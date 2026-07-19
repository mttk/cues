"""Sweep driver: models x sources x conditions, one model load per model,
baseline computed once per model+dataset+subset and reused across all
sources.

Usage:
  python sweep.py --n 100                              # everything (mmlu)
  python sweep.py --models olmo3-7b-think qwen3-8b-think --sources "my mom" "my rock"
  python sweep.py --conditions flip                    # skip placebo
  python sweep.py --dataset medqa --n 100
  python sweep.py --dataset agieval --subset lsat-lr --n 100

Resumable: existing result files are skipped unless --overwrite.
"""

import argparse
import json
from pathlib import Path

from hint_eval import (
    CONDITIONS, MODELS, SOURCES,
    baseline_cache_path, filter_by_length, free_model, legacy_mmlu_baseline_cache_path,
    load_model, maybe_warn_max_new_tokens, result_tag, run_baseline, run_condition,
    save_results, summarize,
)
from qa_datasets import DATASETS, load_qa, validate_subset


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--models", nargs="+", default=list(MODELS), choices=MODELS)
    ap.add_argument("--sources", nargs="+", default=SOURCES)
    ap.add_argument("--conditions", nargs="+", default=CONDITIONS, choices=CONDITIONS)
    ap.add_argument("--dataset", choices=DATASETS, default="mmlu")
    ap.add_argument("--subset", default=None,
                     help="dataset-dependent (see qa_datasets.DATASET_SUBSET_SPEC); "
                          "defaults to 'high_school_psychology' for --dataset mmlu")
    ap.add_argument("--split", default="test")
    ap.add_argument("--n", type=int, default=50)
    ap.add_argument("--max-new-tokens", type=int, default=1536)
    ap.add_argument("--max-question-chars", type=int, default=6000)
    ap.add_argument("--hint-avoid-gold", action=argparse.BooleanOptionalAction, default=True,
                     help="avoid-set for hint sampling is {baseline_answer, gold} instead of "
                          "just {baseline_answer} (default: on) — see hint_eval.py --help")
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--out", default="results")
    ap.add_argument("--overwrite", action="store_true")
    args = ap.parse_args()

    if args.dataset == "mmlu" and args.subset is None:
        args.subset = "high_school_psychology"
    try:
        validate_subset(args.dataset, args.subset)
    except ValueError as e:
        ap.error(str(e))

    data = load_qa(args.dataset, args.subset, args.split, args.n, args.seed)
    data, n_skipped_long = filter_by_length(data, args.max_question_chars)
    if n_skipped_long:
        print(f"[{args.dataset}] skipped {n_skipped_long} item(s) over --max-question-chars {args.max_question_chars}")

    outdir = Path(args.out)
    all_summaries = []

    for mname in args.models:
        # Skip loading the model entirely if every cell for it is done.
        todo = [
            (src, cond) for src in args.sources for cond in args.conditions
            if args.overwrite
            or not (outdir / f"{result_tag(mname, src, args.dataset, args.subset, cond)}.jsonl").exists()
        ]
        if not todo:
            print(f"[{mname}] all cells present, skipping")
            continue

        maybe_warn_max_new_tokens(mname, args.dataset, args.max_new_tokens)

        print(f"[{mname}] loading ({len(todo)} cells to run)")
        model, tok, cfg = load_model(mname)
        cache = baseline_cache_path(outdir, mname, args.dataset, args.subset, args.n, args.seed)
        legacy_caches = (
            [legacy_mmlu_baseline_cache_path(outdir, mname, args.subset, args.n)]
            if args.dataset == "mmlu" else []
        )
        base = run_baseline(model, tok, cfg, data, args.max_new_tokens,
                            cache_path=cache, legacy_cache_paths=legacy_caches)

        for src, cond in todo:
            records, n_skipped_no_letter = run_condition(
                model, tok, cfg, data, base, src, cond, args.seed, args.max_new_tokens,
                args.dataset, hint_avoid_gold=args.hint_avoid_gold,
            )
            meta = dict(model=mname, source=src, dataset=args.dataset, subset=args.subset,
                       n_skipped_long_question=n_skipped_long,
                       n_skipped_no_hint_letter=n_skipped_no_letter)
            summary = summarize(records, base, cond, meta)
            all_summaries.append(summary)
            save_results(records, summary, outdir,
                         result_tag(mname, src, args.dataset, args.subset, cond))
            print(json.dumps(summary, indent=2))

        free_model(model)

    # Aggregate table across the sweep (including previously-completed cells).
    rows = []
    for f in sorted(outdir.glob("*.summary.json")):
        with open(f) as fh:
            rows.append(json.load(fh))
    with open(outdir / "sweep_summaries.json", "w") as fh:
        json.dump(rows, fh, indent=2)
    print(f"\n[done] {len(rows)} summaries -> {outdir/'sweep_summaries.json'}")


if __name__ == "__main__":
    main()
