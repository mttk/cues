# Task: Add a dataset registry with MedQA, LogiQA 2.0, GSM-MC, AGIEval, MMLU-Pro

You are working in the hint-evaluation repo (`hint_eval.py`, `sweep.py`,
`judge.py`). Add support for five new MCQA datasets behind a registry, and
generalize the currently MMLU-specific assumptions. Do not break the existing
MMLU pipeline or the naming of already-produced result files.

## 1. Create `qa_datasets.py` — the registry

One public function per the interface:

```python
def load_qa(dataset: str, subset: str | None, split: str, n: int, seed: int) -> list[dict]
```

Each returned item is normalized to:
```python
{"question": str,        # includes any passage/context, prepended
 "choices": list[str],   # 2..10 options, original order
 "answer": int,          # index into choices
 "qid": str}             # stable id: f"{dataset}:{subset}:{orig_index}"
```

Registry entries (verify each HF id loads before wiring it in; if an id is
wrong, search the Hub for the dataset name and use the closest
well-downloaded variant, and record what you chose in the README):

- **mmlu** (existing behavior, moved here): `cais/mmlu`, subset required,
  `test` split. 4 options.
- **mmlu_pro**: `TIGER-Lab/MMLU-Pro`, `test` split. Fields: `question`,
  `options` (up to 10), `answer_index` (int) / `answer` (letter) — use
  `answer_index`. `subset` filters on the `category` field (optional; None =
  all categories). Drop questions with fewer than 4 options if any.
- **medqa**: `GBaker/MedQA-USMLE-4-options` (or the closest maintained
  USMLE 4/5-option variant), `test` split. Fields typically `question`,
  `options` (dict letter->text), `answer_idx` (letter): sort options by
  letter, map answer letter to index.
- **logiqa2**: LogiQA 2.0 — try `baber/logiqa2` (MC config), `test` split.
  Items have a passage (`text`), `question`, `options` (4), `answer` (int).
  Set `question = passage + "\n\n" + question`.
- **gsm_mc**: search the Hub for a GSM8K multiple-choice conversion
  ("GSM-MC" / "gsm8k mc"). If none loads cleanly, IMPLEMENT THE FALLBACK:
  load `openai/gsm8k` (main, test), parse the gold numeric answer (after
  `####`), and generate 3 deterministic distractors per question with a
  seeded RNG (e.g., gold±10%, gold±1 order-of-magnitude digit swap, off-by-
  one on an intermediate-looking value; dedupe, keep numeric formatting
  consistent), shuffle with the seed, record answer index. Document the
  distractor scheme in the README.
- **agieval**: use the lm-eval-harness exports, configs like
  `hails/agieval-lsat-ar`, `hails/agieval-lsat-lr`, `hails/agieval-lsat-rc`,
  `hails/agieval-logiqa-en`, `hails/agieval-sat-math` — `subset` selects the
  task (required; default `lsat-ar`). Fields: `query`, `choices`, `gold`
  (list; keep only items with exactly one gold). Strip any embedded
  "A." / "(A)" prefixes from choices if present (check!). English MC tasks
  only; skip cloze tasks.

General rules for all loaders: deterministic subsampling (seeded shuffle,
then take first n — NOT `.select(range(n))`, which biases toward the file
head; keep `.select(range(n))` only for `mmlu` to preserve comparability
with existing results, and note this in the README); skip and count items
with missing fields; return fewer than n rather than crash if the split is
small.

## 2. Generalize the option-count assumptions in `hint_eval.py`

Currently hardcoded to `LETTERS = ["A","B","C","D"]`. Change to:

- Per-question letters: `letters(q) = string.ascii_uppercase[:len(q["choices"])]`.
- `build_prompt` uses per-question letters.
- `extract_answer(text, n_options)`: regex letter class built from the actual
  option count (up to J for MMLU-Pro). Keep "last match wins" semantics for
  both the `Answer: X` pattern and the parenthesised fallback, but only
  accept letters within range.
- Hint-letter sampling: sample from that question's letters. ADD a
  `--hint-avoid-gold` flag (DEFAULT ON): the avoid-set becomes
  {baseline_answer, gold}, eliminating the hint_is_gold confound found in the
  uptake analysis. With the flag off, old behavior (avoid baseline only).
  Always record `hint_is_gold` in the record either way. If the avoid-set
  leaves no letters (2-option questions where baseline==wrong option), skip
  the item and count it.
- `gold` in records: store the letter AND `gold_index`; letters beyond D must
  round-trip through the summary code — grep for any remaining `LETTERS`
  uses (there is one inside `summarize`) and fix them.

## 3. Wire through CLI, cache keys, tags

- `hint_eval.py` and `sweep.py` gain `--dataset` (choices from the registry,
  default `mmlu`) and keep `--subset` (now optional, dataset-dependent;
  validate the combination and fail with a helpful message).
- Baseline cache key: `{model}__{dataset}__{subset or 'all'}__n{n}__s{seed}.jsonl`.
  Existing MMLU caches must remain readable: if `--dataset mmlu`, first look
  for the old-format cache name before recomputing.
- `result_tag(...)` gains the dataset: `{model}__{source}__{dataset}__{subset
  or 'all'}__{condition}`. Old MMLU files on disk keep their names; the
  analysis script should treat missing-dataset filenames as `mmlu` (update
  `analysis/uptake_analysis.py` filename parsing accordingly).
- Records gain `dataset`, `qid`, `n_options`, `gold_index`, `hint_is_gold`.

## 4. Budget guards

- Add `--max-question-chars` (default 6000): skip longer items (LogiQA2
  passages and AGIEval RC can be long), count skips in the summary.
- Default `--max-new-tokens` stays 1536, but print a warning recommending
  4096 when `--dataset` is gsm_mc or agieval and the model is a thinking
  variant (parse-rate collapse risk).

## 5. Tests (must run without GPU or network where possible)

- Unit tests with hand-built rows mimicking each dataset's raw schema ->
  assert the normalized format (esp. MedQA letter->index mapping, MMLU-Pro
  10-option letters, AGIEval gold-list handling, GSM-MC fallback distractor
  determinism: same seed -> same choices).
- `extract_answer` tests: "Answer: J" accepted for 10-option, rejected for
  4-option; parenthesised fallback respects range.
- Hint-sampling test: with --hint-avoid-gold, hint never equals gold or
  baseline across 1000 seeded draws; 2-option skip path works.
- A `--dry-run` mode in hint_eval.py that loads the dataset, builds and
  prints 2 formatted prompts (one hinted) and exits — for eyeballing each
  new dataset without a model. Run it once per dataset (network needed) and
  paste one example prompt per dataset into the README.

## 6. Constraints

- tqdm on all loops over data/files.
- Do not modify anything under `results/`.
- Keep `qa_datasets.py` free of torch/transformers imports so judge/analysis
  tooling can import it cheaply.
- Update README: registry table (name, HF id actually used, options count,
  subset semantics, split, any caveats), the GSM-MC fallback scheme if used,
  and a changed-defaults note (`--hint-avoid-gold` on by default — flag this
  loudly since it changes the uptake definition relative to existing runs).
