#!/usr/bin/env python3
"""Retroactively flag parse integrity on existing results/*.jsonl.

No GPU needed: each record's `baseline_output` / `hinted_output` text is
reclassified with the same rules hint_eval.py now applies at generation
time (see parsing.classify_parse) — the parenthesised-letter fallback is
disabled for thinking models, since on a truncated generation (no
`</think>`) it grabs the last option mentioned in the unfinished scratchpad,
which is biased toward the hinted option and manufactures spurious uptake.

Never modifies `results/` — writes flagged records to a sibling
`results_flagged/` directory, mirroring filenames, and regenerates every
`*.summary.json` there (merging the new integrity fields into whatever the
original summary had). Idempotent: rerunning overwrites results_flagged/
deterministically.

Adds to every record:
  base_parse_method, base_think_unclosed   — baseline_output classification
  parse_method, think_unclosed             — hinted_output classification
  clean                    = both sides' parse_method == "explicit"
  answer_strict            = hinted_answer, recomputed under the new rules
  baseline_answer_strict   = baseline_answer, recomputed under the new rules
  parse_changed            = answer_strict != hinted_answer
  baseline_parse_changed   = baseline_answer_strict != baseline_answer
`hinted_answer`/`baseline_answer` themselves are NEVER overwritten
(provenance) — answer_strict/baseline_answer_strict are the "what would we
get under today's rules" companions.

The thinking-model set for retroactive classification comes from the
model-name prefix in the filename (everything before the first `__`) +
models.MODELS; a prefix that isn't in the registry is treated as
non-thinking (the conservative default — keeps the fallback enabled rather
than risk over-flagging an unrecognized model's clean answers as dirty)
and reported at the end so it doesn't pass silently.

Usage:
  python analysis/backfill_parse_flags.py
"""

import json
import sys
from pathlib import Path

import pandas as pd
from tqdm import tqdm

REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from models import MODELS  # noqa: E402  (needs REPO_ROOT on sys.path first)
from parsing import classify_parse  # noqa: E402

RESULTS_DIR = REPO_ROOT / "results"
OUT_DIR = REPO_ROOT / "results_flagged"

# Legacy pre-dataset-registry mmlu records don't carry n_options at all
# (mmlu is 4-way A-D) — same fallback convention as analysis/uptake_analysis.py.
N_OPTIONS_DEFAULT = 4


def find_result_files():
    files = sorted(RESULTS_DIR.glob("*.jsonl"))
    return [f for f in files if not f.name.endswith(".judged.jsonl")]


def parse_model_from_filename(path):
    return path.name.split("__", 1)[0]


def is_thinking_model(model_name, unknown_models):
    if model_name not in MODELS:
        unknown_models.add(model_name)
        return False
    return MODELS[model_name].get("thinking", False)


def flag_record(rec, is_thinking):
    n_opts = rec.get("n_options") or N_OPTIONS_DEFAULT
    baseline_text = rec.get("baseline_output") or ""
    hinted_text = rec.get("hinted_output") or ""

    base_answer, base_parse_method, base_think_unclosed = classify_parse(baseline_text, n_opts, is_thinking)
    hint_answer, parse_method, think_unclosed = classify_parse(hinted_text, n_opts, is_thinking)

    rec["base_parse_method"] = base_parse_method
    rec["base_think_unclosed"] = base_think_unclosed
    rec["parse_method"] = parse_method
    rec["think_unclosed"] = think_unclosed
    rec["clean"] = (parse_method == "explicit") and (base_parse_method == "explicit")
    rec["answer_strict"] = hint_answer
    rec["baseline_answer_strict"] = base_answer
    rec["parse_changed"] = hint_answer != rec.get("hinted_answer")
    rec["baseline_parse_changed"] = base_answer != rec.get("baseline_answer")
    return rec


def primary_hit_field(condition):
    """Which pre-existing bool field represents 'the effect of interest'
    for the before-vs-after-clean rate comparison. flip's legacy `uptake`
    name is kept for continuity; every other condition uses `answer_changed`
    (the left_baseline alias present on every record regardless of era)."""
    return "uptake" if condition == "flip" else "answer_changed"


def rate(records, key):
    vals = [bool(r[key]) for r in records if r.get(key) is not None]
    return sum(vals) / len(vals) if vals else float("nan")


def summarize_flagged(records, original_summary):
    n = len(records)
    condition = records[0].get("condition") if records else original_summary.get("condition")
    clean_records = [r for r in records if r["clean"]]
    hit_field = primary_hit_field(condition)

    summary = dict(original_summary)
    summary.update({
        "condition": condition,
        "n": n,
        "n_clean": len(clean_records),
        "p_clean": len(clean_records) / n if n else float("nan"),
        "n_fallback": sum(r["parse_method"] == "fallback" or r["base_parse_method"] == "fallback" for r in records),
        "n_none": sum(r["parse_method"] == "none" or r["base_parse_method"] == "none" for r in records),
        "n_think_unclosed": sum(bool(r["think_unclosed"]) or bool(r["base_think_unclosed"]) for r in records),
        "n_parse_changed": sum(r["parse_changed"] or r["baseline_parse_changed"] for r in records),
        "hit_field": hit_field,
        f"{hit_field}_rate_all": rate(records, hit_field),
        f"{hit_field}_rate_clean": rate(clean_records, hit_field),
        "has_parse_flags": True,
    })
    return summary


def process_file(fp, unknown_models):
    model_name = parse_model_from_filename(fp)
    thinking = is_thinking_model(model_name, unknown_models)

    with fp.open() as f:
        records = [json.loads(line) for line in f if line.strip()]
    flagged = [flag_record(dict(r), thinking) for r in records]

    out_path = OUT_DIR / fp.name
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w") as f:
        for r in flagged:
            f.write(json.dumps(r) + "\n")

    summary_src = fp.with_name(fp.stem + ".summary.json")
    original_summary = {}
    if summary_src.exists():
        with summary_src.open() as f:
            original_summary = json.load(f)
    summary = summarize_flagged(flagged, original_summary)
    with (OUT_DIR / (fp.stem + ".summary.json")).open("w") as f:
        json.dump(summary, f, indent=2)

    hit_field = summary["hit_field"]
    return {
        "file": fp.name,
        "n": summary["n"],
        "n_clean": summary["n_clean"],
        "n_fallback": summary["n_fallback"],
        "n_none": summary["n_none"],
        "n_think_unclosed": summary["n_think_unclosed"],
        "n_parse_changed": summary["n_parse_changed"],
        f"{hit_field}_all": summary[f"{hit_field}_rate_all"],
        f"{hit_field}_clean": summary[f"{hit_field}_rate_clean"],
    }


def main():
    files = find_result_files()
    if not files:
        print(f"No .jsonl files found under {RESULTS_DIR}. Nothing to backfill.", file=sys.stderr)
        sys.exit(1)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    unknown_models = set()
    rows = []
    for fp in tqdm(files, desc="backfilling parse flags"):
        rows.append(process_file(fp, unknown_models))

    table = pd.DataFrame(rows)
    with pd.option_context("display.max_rows", None, "display.width", 200):
        print("\n" + table.round(3).to_string(index=False))

    n_total = int(table["n"].sum())
    n_clean_total = int(table["n_clean"].sum())
    print(f"\n[done] {len(files)} file(s) -> {OUT_DIR}")
    print(f"[done] {n_clean_total}/{n_total} records clean overall ({n_clean_total / n_total:.1%})")
    if unknown_models:
        print(f"[warn] {len(unknown_models)} model name(s) not found in models.MODELS "
              f"(treated as non-thinking, fallback left enabled): {sorted(unknown_models)}", file=sys.stderr)


if __name__ == "__main__":
    main()
