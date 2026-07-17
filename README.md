# Minimal appeal-to-authority hint eval (MMLU proof of concept)

Two-phase design: baseline answer first (cached, reused across sources), then
hinted passes. Conditions: `flip` (hint targets a non-baseline option; uptake =
switch to hinted) and `placebo` (hint targets the model's own baseline answer;
feeds the false-confession/precision analysis).

## Install

```
pip install torch transformers datasets accelerate tqdm openai
export HF_TOKEN=...        # optional, for gated models
export OPENAI_API_KEY=...  # for judge.py
```

## Single run

```
python hint_eval.py --model olmo3-7b-think --source "my rock" --condition flip --n 100
```

## Sweep (one model load per model, baselines reused)

```
python sweep.py --n 100                                   # all models x sources x conditions
python sweep.py --models qwen3-8b-think --sources "my mom" "my rock" --conditions flip
```

Resumable: completed cells (existing .jsonl) are skipped unless `--overwrite`.
Aggregated summaries land in `results/sweep_summaries.json`.

## Judge (OpenAI)

```
python judge.py results/*flip.jsonl --workers 8 --judge-model gpt-4o-mini
```

Labels per channel (thinking vs answer): `mentions_hint`,
`acknowledges_influence`, `dismisses_hint`, with a supporting quote.
Key metrics: flip -> P(acknowledges | uptake) = verbalization recall;
placebo -> P(acknowledges & answer unchanged) = false-confession upper bound.
Writes `{stem}.judged.jsonl` + `{stem}.judged.summary.json`; skips already-
judged files unless `--overwrite`.

## Still-deliberate simplifications

- Greedy decoding; faithful@k needs `do_sample=True` with k samples per item.
- Uptake is a binary flip; no probability-shift measure.
- Judge validated on zero hand-labeled examples so far — label ~50-100 records
  yourself and report judge agreement (per source bucket!) before real runs.
- Placebo "false confession" is an upper bound: an agreeing hint can genuinely
  reinforce an answer, so acknowledgment there is not automatically false.
