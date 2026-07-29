#!/usr/bin/env python3
"""Retroactively flag parse integrity on existing *.judged.jsonl files.

Existing judged files were produced before the parse-integrity fields
existed. This applies the exact same reclassification as
backfill_parse_flags.py (imported directly from there — flag_record is not
duplicated) to each judged record, and recomputes the judge summary with:
  contains_dirty        — True if any record in the file is not clean
  n_clean, p_clean       — clean-record count/fraction
  {metric}_clean         — every judge-summary metric (see judge_metrics.
                           summarize_judged), recomputed on clean records
                           only, e.g. p_ack_answer_given_uptake_clean. The
                           qwen-think judged batches are known to be
                           heavily dirty (see backfill_parse_flags.py's
                           output) — expect their clean-only n to be tiny.

Never modifies results/ — writes flagged records + updated summaries to the
same sibling results_flagged/ directory backfill_parse_flags.py uses,
mirroring filenames. No GPU/network needed: reclassifies from the stored
baseline_output/hinted_output text; the judge model is never called again.

Usage:
  python analysis/backfill_judged_flags.py
"""

import json
import sys
from pathlib import Path

import pandas as pd
from tqdm import tqdm

REPO_ROOT = Path(__file__).resolve().parent.parent
ANALYSIS_DIR = Path(__file__).resolve().parent
for p in (REPO_ROOT, ANALYSIS_DIR):
    if str(p) not in sys.path:
        sys.path.insert(0, str(p))

from backfill_parse_flags import flag_record, is_thinking_model, parse_model_from_filename  # noqa: E402
from judge_metrics import summarize_judged  # noqa: E402

RESULTS_DIR = REPO_ROOT / "results"
OUT_DIR = REPO_ROOT / "results_flagged"


def find_judged_files():
    return sorted(RESULTS_DIR.glob("*.judged.jsonl"))


def summarize_judged_with_clean_split(records):
    summary = summarize_judged(records)
    clean_records = [r for r in records if r.get("clean")]
    n, n_clean = len(records), len(clean_records)
    summary["n_clean"] = n_clean
    summary["p_clean"] = n_clean / n if n else float("nan")
    summary["contains_dirty"] = n_clean < n
    clean_summary = summarize_judged(clean_records)
    for k, v in clean_summary.items():
        if k in ("condition", "n", "source"):
            continue
        summary[f"{k}_clean"] = v
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

    summary = summarize_judged_with_clean_split(flagged)
    with (OUT_DIR / (fp.stem + ".summary.json")).open("w") as f:  # {stem}.judged.summary.json
        json.dump(summary, f, indent=2)

    return {
        "file": fp.name, "n": len(flagged), "n_clean": summary["n_clean"],
        "p_clean": summary["p_clean"], "contains_dirty": summary["contains_dirty"],
    }


def main():
    files = find_judged_files()
    if not files:
        print(f"No .judged.jsonl files found under {RESULTS_DIR}. Nothing to backfill.", file=sys.stderr)
        sys.exit(1)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    unknown_models = set()
    rows = [process_file(fp, unknown_models) for fp in tqdm(files, desc="backfilling judged flags")]

    table = pd.DataFrame(rows)
    with pd.option_context("display.max_rows", None, "display.width", 200):
        print("\n" + table.round(3).to_string(index=False))
    print(f"\n[done] {len(files)} file(s) -> {OUT_DIR}")
    if unknown_models:
        print(f"[warn] {len(unknown_models)} model name(s) not found in models.MODELS "
              f"(treated as non-thinking, fallback left enabled): {sorted(unknown_models)}", file=sys.stderr)


if __name__ == "__main__":
    main()
