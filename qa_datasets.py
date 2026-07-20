"""MCQA dataset registry, normalized to a single item shape:

    {"question": str,        # includes any passage/context, prepended
     "choices": list[str],   # 2..10 options, original order
     "answer": int,          # index into choices
     "qid": str}             # stable id: f"{dataset}:{subset}:{orig_index}"

Public entry point: `load_qa(dataset, subset, split, n, seed)`.

Kept free of torch/transformers so judge.py and the analysis scripts can
import this module cheaply. `datasets` (the HF library) is imported lazily
inside each loader so that hand-built-row unit tests (see tests/) never need
network access or the `datasets` package installed.
"""

import json
import random
import re

from tqdm import tqdm

DATASETS = ["mmlu", "mmlu_pro", "medqa", "logiqa2", "gsm_mc", "agieval"]

# How each dataset treats --subset, used by validate_subset() for CLI
# error messages:
#   "required" -> must be a non-empty string (mmlu: any MMLU config name;
#                 agieval: one of AGIEVAL_CONFIGS, defaults to "lsat-ar")
#   "optional" -> string filters, None means "all" (mmlu_pro: category)
#   "none"     -> dataset has no subset concept; must be left as None
DATASET_SUBSET_SPEC = {
    "mmlu": "required",
    "mmlu_pro": "optional",
    "medqa": "none",
    "logiqa2": "none",
    "gsm_mc": "none",
    "agieval": "required",
}

# lm-eval-harness AGIEval exports actually used here. Only the English,
# non-cloze multiple-choice tasks named in the task spec are wired in.
AGIEVAL_CONFIGS = {
    "lsat-ar": "hails/agieval-lsat-ar",
    "lsat-lr": "hails/agieval-lsat-lr",
    "lsat-rc": "hails/agieval-lsat-rc",
    "logiqa-en": "hails/agieval-logiqa-en",
    "sat-math": "hails/agieval-sat-math",
}

# Raw HF dataset ids actually wired in (see README for what was verified /
# why each was chosen over alternatives).
HF_IDS = {
    "mmlu": "cais/mmlu",
    "mmlu_pro": "TIGER-Lab/MMLU-Pro",
    "medqa": "GBaker/MedQA-USMLE-4-options",
    "logiqa2": "datatune/LogiQA2.0",
    "gsm_mc": "guipenedo/gsm8k-mc",
    **AGIEVAL_CONFIGS,
}

_AGIEVAL_PREFIX_RE = re.compile(r"^(\([A-Z]\)|[A-Z][.:])\s*")


def validate_subset(dataset, subset):
    """Raise ValueError with a helpful message if (dataset, subset) is an
    invalid combination. Does not require network access."""
    if dataset not in DATASET_SUBSET_SPEC:
        raise ValueError(f"unknown dataset {dataset!r}; choices: {DATASETS}")
    spec = DATASET_SUBSET_SPEC[dataset]
    if spec == "required" and dataset == "mmlu" and not subset:
        raise ValueError(
            "dataset 'mmlu' requires --subset (an MMLU config name, "
            "e.g. high_school_psychology)"
        )
    if spec == "required" and dataset == "agieval" and subset is not None and subset not in AGIEVAL_CONFIGS:
        raise ValueError(
            f"dataset 'agieval' --subset must be one of {sorted(AGIEVAL_CONFIGS)} "
            f"(or omitted, defaults to 'lsat-ar'), got {subset!r}"
        )
    if spec == "none" and subset is not None:
        raise ValueError(
            f"dataset {dataset!r} does not take --subset (got {subset!r}); omit it"
        )


# --------------------------------------------------------------------------
# Deterministic subsampling shared by every loader except mmlu (mmlu keeps
# .select(range(n)) to stay bit-for-bit comparable with existing results).
# --------------------------------------------------------------------------

def _seeded_take(candidates, n, seed, normalize_fn, desc):
    """candidates: list of (orig_idx, raw_row). Seeded-shuffle the order,
    then take the first n rows for which normalize_fn succeeds (returns a
    dict, not None). Returns (items, n_skipped); never crashes on n >
    len(candidates), just returns fewer items."""
    order = list(range(len(candidates)))
    random.Random(seed).shuffle(order)
    items = []
    skipped = 0
    for pos in tqdm(order, desc=desc):
        if len(items) >= n:
            break
        orig_idx, raw = candidates[pos]
        item = normalize_fn(orig_idx, raw)
        if item is None:
            skipped += 1
            continue
        items.append(item)
    return items, skipped


# --------------------------------------------------------------------------
# mmlu (existing behavior, moved here unchanged)
# --------------------------------------------------------------------------

def _load_mmlu(subset, split, n, seed):
    from datasets import load_dataset

    ds = load_dataset(HF_IDS["mmlu"], subset, split=split)
    ds = ds.select(range(min(n, len(ds))))
    items = []
    for i, row in enumerate(tqdm(ds, desc="mmlu")):
        items.append({
            "question": row["question"],
            "choices": list(row["choices"]),
            "answer": int(row["answer"]),
            "qid": f"mmlu:{subset}:{i}",
        })
    return items


# --------------------------------------------------------------------------
# mmlu_pro
# --------------------------------------------------------------------------

def _normalize_mmlu_pro(orig_idx, row, subset):
    opts = list(row["options"])
    if len(opts) < 4:
        return None
    ans_idx = row.get("answer_index")
    if ans_idx is None or not (0 <= ans_idx < len(opts)):
        return None
    return {
        "question": row["question"],
        "choices": opts,
        "answer": int(ans_idx),
        "qid": f"mmlu_pro:{subset or 'all'}:{orig_idx}",
    }


def _load_mmlu_pro(subset, split, n, seed):
    from datasets import load_dataset

    ds = load_dataset(HF_IDS["mmlu_pro"], split=split)
    candidates = [
        (i, row) for i, row in enumerate(tqdm(ds, desc="mmlu_pro:scan"))
        if subset is None or row["category"] == subset
    ]
    items, skipped = _seeded_take(
        candidates, n, seed,
        lambda idx, row: _normalize_mmlu_pro(idx, row, subset),
        desc="mmlu_pro:sample",
    )
    if skipped:
        print(f"[mmlu_pro] skipped {skipped} candidate(s) with <4 options")
    return items


# --------------------------------------------------------------------------
# medqa
# --------------------------------------------------------------------------

def _normalize_medqa(orig_idx, row, subset):
    opts = row.get("options")
    ans_letter = row.get("answer_idx")
    question = row.get("question")
    if not opts or not ans_letter or not question:
        return None
    letters = sorted(opts.keys())
    if ans_letter not in letters:
        return None
    return {
        "question": question,
        "choices": [opts[l] for l in letters],
        "answer": letters.index(ans_letter),
        "qid": f"medqa:{subset or 'all'}:{orig_idx}",
    }


def _load_medqa(subset, split, n, seed):
    from datasets import load_dataset

    ds = load_dataset(HF_IDS["medqa"], split=split)
    candidates = list(enumerate(tqdm(ds, desc="medqa:scan")))
    items, skipped = _seeded_take(
        candidates, n, seed,
        lambda idx, row: _normalize_medqa(idx, row, subset),
        desc="medqa:sample",
    )
    if skipped:
        print(f"[medqa] skipped {skipped} candidate(s) with missing fields")
    return items


# --------------------------------------------------------------------------
# logiqa2 — datatune/LogiQA2.0. Every split is a single `text` column whose
# value is itself a JSON-encoded string, and the rows are an undifferentiated
# mix of three original LogiQA 2.0 configs: the English MC set we want
# ({question, options, answer, text}), its Chinese translation (same shape,
# CJK content), and an NLI-reformulated set ({premise, hypothesis, label},
# no `options`). _load_logiqa2 parses the JSON wrapper and _normalize_logiqa2
# filters to the English MC rows only (dropped: NLI rows lack `options` and
# are skipped by the missing-field check; Chinese rows are dropped by the CJK
# check). Verified this recovers exactly 1572 English MC test rows, matching
# the original LogiQA 2.0 English test set size.
# --------------------------------------------------------------------------

_CJK_RE = re.compile(r"[一-鿿]")


def _normalize_logiqa2(orig_idx, row, subset):
    """`row` is the dict already parsed from the raw `text` JSON string (see
    _load_logiqa2) — not the raw HF row itself."""
    opts = row.get("options")
    ans = row.get("answer")
    question = row.get("question")
    if not opts or ans is None or not question:
        return None
    if not (0 <= ans < len(opts)):
        return None
    passage = row.get("text") or ""
    if _CJK_RE.search(question + "".join(opts) + passage):
        return None  # Chinese-language counterpart row; English MC only
    full_question = f"{passage}\n\n{question}" if passage else question
    return {
        "question": full_question,
        "choices": list(opts),
        "answer": int(ans),
        "qid": f"logiqa2:{subset or 'all'}:{orig_idx}",
    }


def _load_logiqa2(subset, split, n, seed):
    from datasets import load_dataset

    ds = load_dataset(HF_IDS["logiqa2"], split=split)
    candidates = []
    n_parse_fail = 0
    for i, raw_row in enumerate(tqdm(ds, desc="logiqa2:scan")):
        try:
            candidates.append((i, json.loads(raw_row["text"])))
        except (json.JSONDecodeError, TypeError):
            n_parse_fail += 1
    if n_parse_fail:
        print(f"[logiqa2] skipped {n_parse_fail} row(s) with malformed JSON in the raw `text` field")
    items, skipped = _seeded_take(
        candidates, n, seed,
        lambda idx, row: _normalize_logiqa2(idx, row, subset),
        desc="logiqa2:sample",
    )
    if skipped:
        print(f"[logiqa2] skipped {skipped} candidate(s) with missing fields or non-English (Chinese) content")
    return items


# --------------------------------------------------------------------------
# gsm_mc — guipenedo/gsm8k-mc loads cleanly (verified: 1319 test rows, A-D +
# Answer + Question, no missing fields, balanced answer letters), so the
# synthetic-distractor fallback described in the task spec was not needed.
# --------------------------------------------------------------------------

_GSM_MC_LETTERS = ["A", "B", "C", "D"]


def _normalize_gsm_mc(orig_idx, row, subset):
    question = row.get("Question")
    ans_letter = row.get("Answer")
    if not question or ans_letter not in _GSM_MC_LETTERS:
        return None
    try:
        choices = [str(row[l]) for l in _GSM_MC_LETTERS]
    except KeyError:
        return None
    return {
        "question": question,
        "choices": choices,
        "answer": _GSM_MC_LETTERS.index(ans_letter),
        "qid": f"gsm_mc:{subset or 'all'}:{orig_idx}",
    }


def _load_gsm_mc(subset, split, n, seed):
    from datasets import load_dataset

    ds = load_dataset(HF_IDS["gsm_mc"], split=split)
    candidates = list(enumerate(tqdm(ds, desc="gsm_mc:scan")))
    items, skipped = _seeded_take(
        candidates, n, seed,
        lambda idx, row: _normalize_gsm_mc(idx, row, subset),
        desc="gsm_mc:sample",
    )
    if skipped:
        print(f"[gsm_mc] skipped {skipped} candidate(s) with missing fields")
    return items


# --------------------------------------------------------------------------
# agieval
# --------------------------------------------------------------------------

def _normalize_agieval(orig_idx, row, subset):
    gold = row.get("gold")
    choices_raw = row.get("choices")
    query = row.get("query")
    if not gold or len(gold) != 1 or not choices_raw or query is None:
        return None
    answer = gold[0]
    if not (0 <= answer < len(choices_raw)):
        return None
    choices = [_AGIEVAL_PREFIX_RE.sub("", c, count=1) for c in choices_raw]
    return {
        "question": query,
        "choices": choices,
        "answer": int(answer),
        "qid": f"agieval:{subset}:{orig_idx}",
    }


def _load_agieval(subset, split, n, seed):
    from datasets import load_dataset

    subset = subset or "lsat-ar"
    ds = load_dataset(AGIEVAL_CONFIGS[subset], split=split)
    candidates = list(enumerate(tqdm(ds, desc=f"agieval:{subset}:scan")))
    items, skipped = _seeded_take(
        candidates, n, seed,
        lambda idx, row: _normalize_agieval(idx, row, subset),
        desc=f"agieval:{subset}:sample",
    )
    if skipped:
        print(f"[agieval:{subset}] skipped {skipped} candidate(s) with missing/multi gold")
    return items


_LOADERS = {
    "mmlu": _load_mmlu,
    "mmlu_pro": _load_mmlu_pro,
    "medqa": _load_medqa,
    "logiqa2": _load_logiqa2,
    "gsm_mc": _load_gsm_mc,
    "agieval": _load_agieval,
}


def load_qa(dataset, subset, split, n, seed):
    """Load and normalize n items of `dataset` (optionally filtered to
    `subset`) from `split`, deterministically subsampled by `seed`."""
    if dataset not in _LOADERS:
        raise ValueError(f"unknown dataset {dataset!r}; choices: {DATASETS}")
    if dataset == "agieval" and subset is None:
        subset = "lsat-ar"
    validate_subset(dataset, subset)
    return _LOADERS[dataset](subset, split, n, seed)
