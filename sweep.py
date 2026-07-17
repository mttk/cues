"""Sweep driver: models x sources x conditions, one model load per model,
baseline computed once per model+subset and reused across all sources.

Usage:
  python sweep.py --n 100                              # everything
  python sweep.py --models olmo3-7b-think qwen3-8b-think --sources "my mom" "my rock"
  python sweep.py --conditions flip                    # skip placebo

Resumable: existing result files are skipped unless --overwrite.
"""

import argparse
import json
from pathlib import Path

from datasets import load_dataset

from hint_eval import (
    CONDITIONS, MODELS, SOURCES,
    free_model, load_model, result_tag, run_baseline, run_condition,
    save_results, summarize,
)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--models", nargs="+", default=list(MODELS), choices=MODELS)
    ap.add_argument("--sources", nargs="+", default=SOURCES)
    ap.add_argument("--conditions", nargs="+", default=CONDITIONS, choices=CONDITIONS)
    ap.add_argument("--subset", default="high_school_psychology")
    ap.add_argument("--n", type=int, default=50)
    ap.add_argument("--max-new-tokens", type=int, default=1536)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--out", default="results")
    ap.add_argument("--overwrite", action="store_true")
    args = ap.parse_args()

    data = load_dataset("cais/mmlu", args.subset, split="test").select(range(args.n))
    outdir = Path(args.out)
    all_summaries = []

    for mname in args.models:
        # Skip loading the model entirely if every cell for it is done.
        todo = [
            (src, cond) for src in args.sources for cond in args.conditions
            if args.overwrite
            or not (outdir / f"{result_tag(mname, src, args.subset, cond)}.jsonl").exists()
        ]
        if not todo:
            print(f"[{mname}] all cells present, skipping")
            continue

        print(f"[{mname}] loading ({len(todo)} cells to run)")
        model, tok, cfg = load_model(mname)
        cache = outdir / "baselines" / f"{mname}__{args.subset}__n{args.n}.jsonl"
        base = run_baseline(model, tok, cfg, data, args.max_new_tokens, cache_path=cache)

        for src, cond in todo:
            records = run_condition(
                model, tok, cfg, data, base, src, cond, args.seed, args.max_new_tokens
            )
            meta = dict(model=mname, source=src, subset=args.subset)
            summary = summarize(records, base, cond, meta)
            all_summaries.append(summary)
            save_results(records, summary, outdir,
                         result_tag(mname, src, args.subset, cond))
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
