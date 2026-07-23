#!/bin/bash
# Submits the remaining sweep jobs on the cluster:
#   - a full MMLU re-run (mmlu/ was archived to results/mmlu_archive/, so
#     sweep.py sees nothing there and recomputes everything)
#   - the neg_own/neg_other cue experiments, for every model x dataset mix
#     that doesn't have them yet (currently: all of them)
#   - the still-missing flip/placebo base-condition mixes (olmo3-7b-instruct
#     and olmo3-7b-think on agieval; r1-distill-qwen-7b on medqa, logiqa2,
#     agieval)
#
# One sbatch job per (model, dataset), requesting all 4 conditions each
# time. sweep.py's resumability means already-completed cells are skipped
# (not overwritten) - only what's actually missing gets computed. This is
# why the full condition list is passed everywhere rather than
# hand-tracking which specific cells are missing per model/dataset.
#
# MedQA/LogiQA 2.0/AGIEval get --max-new-tokens 4096 (up from the default
# 1536): thinking models were seeing real parse-rate collapse there
# (e.g. qwen3-8b-think baseline parse_rate was 0.27 on AGIEval, 0.75 on
# MedQA, 0.68 on LogiQA at 1536 - see the baseline accuracy table). MMLU
# keeps the default 1536, since it wasn't part of that ask and its parse
# rates were already fine (0.89-1.00 across all 5 models).
#
# Run from the repo root: bash scripts/launch_remaining_sweeps.sh

MODELS="olmo3-7b-instruct olmo3-7b-think qwen3-8b-think qwen3-8b-nothink r1-distill-qwen-7b"
CONDITIONS="flip placebo neg_own neg_other"

echo "=== MMLU: full re-run, all models, --max-new-tokens 1536 ==="
for model in $MODELS; do
    sbatch scripts/sweep_model_custom.sh "$model" mmlu 1536 $CONDITIONS
done

echo "=== MedQA / LogiQA 2.0 / AGIEval: fill missing cells + cue experiments, --max-new-tokens 4096 ==="
for model in $MODELS; do
    for dataset in medqa logiqa2 agieval; do
        sbatch scripts/sweep_model_custom.sh "$model" "$dataset" 4096 $CONDITIONS
    done
done
