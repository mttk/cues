# Uptake analysis report

Generated from `results_flagged`, scope: all datasets (['logiqa2', 'medqa', 'mmlu']) (4 model(s), 9 source(s), conditions present: ['flip', 'placebo', 'neg_own', 'neg_other']).

## Parse integrity

Every headline table/statistic in this report — including all paired stats — is computed on **clean** records only (both the baseline and hinted generations produced an explicit, non-truncated answer; see `parsing.classify_parse`). Of 60138 records loaded in scope, 35297 (58.7%) were excluded as dirty or quarantined, leaving 24841 clean.

Per-(model,dataset) summary (full table: `analysis/uptake_parse_integrity.csv`):

```
             model dataset    n  p_clean  p_fallback  p_think_unclosed  quarantined
 olmo3-7b-instruct agieval 3528    0.494       0.501             0.000         True
 olmo3-7b-instruct logiqa2 3600    0.916       0.081             0.000        False
 olmo3-7b-instruct   medqa 3600    0.885       0.114             0.000        False
 olmo3-7b-instruct    mmlu 3600    0.981       0.019             0.000        False
    olmo3-7b-think agieval 2052    0.000       0.000             0.921         True
    olmo3-7b-think logiqa2 2736    0.408       0.000             0.586         True
    olmo3-7b-think   medqa 2772    0.314       0.000             0.654         True
    olmo3-7b-think    mmlu 3204    0.663       0.000             0.336         True
  qwen3-8b-nothink agieval 3096    0.556       0.409             0.000         True
  qwen3-8b-nothink logiqa2 3564    0.947       0.051             0.000        False
  qwen3-8b-nothink   medqa 3600    0.747       0.251             0.000        False
  qwen3-8b-nothink    mmlu 3600    0.979       0.021             0.000        False
    qwen3-8b-think agieval 1836    0.278       0.000             0.646         True
    qwen3-8b-think logiqa2 2916    0.678       0.000             0.258         True
    qwen3-8b-think   medqa 3078    0.671       0.000             0.281         True
    qwen3-8b-think    mmlu 3492    0.848       0.000             0.135        False
r1-distill-qwen-7b agieval 1404    0.148       0.000             0.733         True
r1-distill-qwen-7b logiqa2 2736    0.656       0.000             0.266         True
r1-distill-qwen-7b   medqa 2520    0.506       0.000             0.278         True
r1-distill-qwen-7b    mmlu 3204    0.710       0.000             0.227        False
```

**Quarantined (p_clean < 70%) — excluded from every table/statistic in this report, not just their dirty records:**

  - olmo3-7b-instruct/agieval: p_clean=49.4% (n=3528)
  - olmo3-7b-think/agieval: p_clean=0.0% (n=2052)
  - olmo3-7b-think/logiqa2: p_clean=40.8% (n=2736)
  - olmo3-7b-think/medqa: p_clean=31.4% (n=2772)
  - olmo3-7b-think/mmlu: p_clean=66.3% (n=3204)
  - qwen3-8b-nothink/agieval: p_clean=55.6% (n=3096)
  - qwen3-8b-think/agieval: p_clean=27.8% (n=1836)
  - qwen3-8b-think/logiqa2: p_clean=67.8% (n=2916)
  - qwen3-8b-think/medqa: p_clean=67.1% (n=3078)
  - r1-distill-qwen-7b/agieval: p_clean=14.8% (n=1404)
  - r1-distill-qwen-7b/logiqa2: p_clean=65.6% (n=2736)
  - r1-distill-qwen-7b/medqa: p_clean=50.6% (n=2520)

The **contamination panel** (full table: `analysis/uptake_contamination.csv`) quantifies the manufactured-uptake artifact directly: per (model, dataset, source, condition), the headline rate (`uptake` for flip, `answer_changed`/left_baseline elsewhere) computed over ALL records vs. over CLEAN records only, plus `p_truncated` (think_unclosed or a non-explicit parse on the hinted side). See the largest `rate_all - rate_clean` gaps there for the cells where this mattered most.

## Missing cells

**Missing flip cells (36):** qwen3-8b-think/logiqa2/a Stanford professor, qwen3-8b-think/logiqa2/a fortune cookie, qwen3-8b-think/logiqa2/a stranger on the bus, qwen3-8b-think/logiqa2/my best friend, qwen3-8b-think/logiqa2/my dog, qwen3-8b-think/logiqa2/my horoscope, qwen3-8b-think/logiqa2/my mom, qwen3-8b-think/logiqa2/my professor, qwen3-8b-think/logiqa2/my rock, qwen3-8b-think/medqa/a Stanford professor, qwen3-8b-think/medqa/a fortune cookie, qwen3-8b-think/medqa/a stranger on the bus, qwen3-8b-think/medqa/my best friend, qwen3-8b-think/medqa/my dog, qwen3-8b-think/medqa/my horoscope, qwen3-8b-think/medqa/my mom, qwen3-8b-think/medqa/my professor, qwen3-8b-think/medqa/my rock, r1-distill-qwen-7b/logiqa2/a Stanford professor, r1-distill-qwen-7b/logiqa2/a fortune cookie, r1-distill-qwen-7b/logiqa2/a stranger on the bus, r1-distill-qwen-7b/logiqa2/my best friend, r1-distill-qwen-7b/logiqa2/my dog, r1-distill-qwen-7b/logiqa2/my horoscope, r1-distill-qwen-7b/logiqa2/my mom, r1-distill-qwen-7b/logiqa2/my professor, r1-distill-qwen-7b/logiqa2/my rock, r1-distill-qwen-7b/medqa/a Stanford professor, r1-distill-qwen-7b/medqa/a fortune cookie, r1-distill-qwen-7b/medqa/a stranger on the bus, r1-distill-qwen-7b/medqa/my best friend, r1-distill-qwen-7b/medqa/my dog, r1-distill-qwen-7b/medqa/my horoscope, r1-distill-qwen-7b/medqa/my mom, r1-distill-qwen-7b/medqa/my professor, r1-distill-qwen-7b/medqa/my rock

**Missing placebo cells (36):** qwen3-8b-think/logiqa2/a Stanford professor, qwen3-8b-think/logiqa2/a fortune cookie, qwen3-8b-think/logiqa2/a stranger on the bus, qwen3-8b-think/logiqa2/my best friend, qwen3-8b-think/logiqa2/my dog, qwen3-8b-think/logiqa2/my horoscope, qwen3-8b-think/logiqa2/my mom, qwen3-8b-think/logiqa2/my professor, qwen3-8b-think/logiqa2/my rock, qwen3-8b-think/medqa/a Stanford professor, qwen3-8b-think/medqa/a fortune cookie, qwen3-8b-think/medqa/a stranger on the bus, qwen3-8b-think/medqa/my best friend, qwen3-8b-think/medqa/my dog, qwen3-8b-think/medqa/my horoscope, qwen3-8b-think/medqa/my mom, qwen3-8b-think/medqa/my professor, qwen3-8b-think/medqa/my rock, r1-distill-qwen-7b/logiqa2/a Stanford professor, r1-distill-qwen-7b/logiqa2/a fortune cookie, r1-distill-qwen-7b/logiqa2/a stranger on the bus, r1-distill-qwen-7b/logiqa2/my best friend, r1-distill-qwen-7b/logiqa2/my dog, r1-distill-qwen-7b/logiqa2/my horoscope, r1-distill-qwen-7b/logiqa2/my mom, r1-distill-qwen-7b/logiqa2/my professor, r1-distill-qwen-7b/logiqa2/my rock, r1-distill-qwen-7b/medqa/a Stanford professor, r1-distill-qwen-7b/medqa/a fortune cookie, r1-distill-qwen-7b/medqa/a stranger on the bus, r1-distill-qwen-7b/medqa/my best friend, r1-distill-qwen-7b/medqa/my dog, r1-distill-qwen-7b/medqa/my horoscope, r1-distill-qwen-7b/medqa/my mom, r1-distill-qwen-7b/medqa/my professor, r1-distill-qwen-7b/medqa/my rock

**Missing neg_own cells (36):** qwen3-8b-think/logiqa2/a Stanford professor, qwen3-8b-think/logiqa2/a fortune cookie, qwen3-8b-think/logiqa2/a stranger on the bus, qwen3-8b-think/logiqa2/my best friend, qwen3-8b-think/logiqa2/my dog, qwen3-8b-think/logiqa2/my horoscope, qwen3-8b-think/logiqa2/my mom, qwen3-8b-think/logiqa2/my professor, qwen3-8b-think/logiqa2/my rock, qwen3-8b-think/medqa/a Stanford professor, qwen3-8b-think/medqa/a fortune cookie, qwen3-8b-think/medqa/a stranger on the bus, qwen3-8b-think/medqa/my best friend, qwen3-8b-think/medqa/my dog, qwen3-8b-think/medqa/my horoscope, qwen3-8b-think/medqa/my mom, qwen3-8b-think/medqa/my professor, qwen3-8b-think/medqa/my rock, r1-distill-qwen-7b/logiqa2/a Stanford professor, r1-distill-qwen-7b/logiqa2/a fortune cookie, r1-distill-qwen-7b/logiqa2/a stranger on the bus, r1-distill-qwen-7b/logiqa2/my best friend, r1-distill-qwen-7b/logiqa2/my dog, r1-distill-qwen-7b/logiqa2/my horoscope, r1-distill-qwen-7b/logiqa2/my mom, r1-distill-qwen-7b/logiqa2/my professor, r1-distill-qwen-7b/logiqa2/my rock, r1-distill-qwen-7b/medqa/a Stanford professor, r1-distill-qwen-7b/medqa/a fortune cookie, r1-distill-qwen-7b/medqa/a stranger on the bus, r1-distill-qwen-7b/medqa/my best friend, r1-distill-qwen-7b/medqa/my dog, r1-distill-qwen-7b/medqa/my horoscope, r1-distill-qwen-7b/medqa/my mom, r1-distill-qwen-7b/medqa/my professor, r1-distill-qwen-7b/medqa/my rock

**Missing neg_other cells (36):** qwen3-8b-think/logiqa2/a Stanford professor, qwen3-8b-think/logiqa2/a fortune cookie, qwen3-8b-think/logiqa2/a stranger on the bus, qwen3-8b-think/logiqa2/my best friend, qwen3-8b-think/logiqa2/my dog, qwen3-8b-think/logiqa2/my horoscope, qwen3-8b-think/logiqa2/my mom, qwen3-8b-think/logiqa2/my professor, qwen3-8b-think/logiqa2/my rock, qwen3-8b-think/medqa/a Stanford professor, qwen3-8b-think/medqa/a fortune cookie, qwen3-8b-think/medqa/a stranger on the bus, qwen3-8b-think/medqa/my best friend, qwen3-8b-think/medqa/my dog, qwen3-8b-think/medqa/my horoscope, qwen3-8b-think/medqa/my mom, qwen3-8b-think/medqa/my professor, qwen3-8b-think/medqa/my rock, r1-distill-qwen-7b/logiqa2/a Stanford professor, r1-distill-qwen-7b/logiqa2/a fortune cookie, r1-distill-qwen-7b/logiqa2/a stranger on the bus, r1-distill-qwen-7b/logiqa2/my best friend, r1-distill-qwen-7b/logiqa2/my dog, r1-distill-qwen-7b/logiqa2/my horoscope, r1-distill-qwen-7b/logiqa2/my mom, r1-distill-qwen-7b/logiqa2/my professor, r1-distill-qwen-7b/logiqa2/my rock, r1-distill-qwen-7b/medqa/a Stanford professor, r1-distill-qwen-7b/medqa/a fortune cookie, r1-distill-qwen-7b/medqa/a stranger on the bus, r1-distill-qwen-7b/medqa/my best friend, r1-distill-qwen-7b/medqa/my dog, r1-distill-qwen-7b/medqa/my horoscope, r1-distill-qwen-7b/medqa/my mom, r1-distill-qwen-7b/medqa/my professor, r1-distill-qwen-7b/medqa/my rock


## Sanity checks

- Multi-source flip/placebo/neg_own/neg_other cells (should be 0): 0
- Baseline-answer mismatches within a (model, dataset) across cells/conditions (should be 0): 0 idx affected
- Recomputed-vs-stored `uptake` mismatches on flip (should be 0): 0
- Recomputed-vs-summary.json discrepancies (should be 0): 213
  - {'model': 'olmo3-7b-instruct', 'dataset': 'mmlu', 'source': 'a Stanford professor', 'condition': 'neg_other', 'field': 'n_clean', 'summary_value': 87, 'recomputed_value': 98}
  - {'model': 'olmo3-7b-instruct', 'dataset': 'mmlu', 'source': 'a Stanford professor', 'condition': 'neg_other', 'field': 'answer_changed_rate_clean', 'summary_value': 0.3563218390804598, 'recomputed_value': np.float64(0.23469387755102042)}
  - {'model': 'olmo3-7b-instruct', 'dataset': 'mmlu', 'source': 'a Stanford professor', 'condition': 'neg_own', 'field': 'n_clean', 'summary_value': 90, 'recomputed_value': 86}
  - {'model': 'olmo3-7b-instruct', 'dataset': 'mmlu', 'source': 'a Stanford professor', 'condition': 'neg_own', 'field': 'answer_changed_rate_clean', 'summary_value': 0.4666666666666667, 'recomputed_value': np.float64(0.3372093023255814)}
  - {'model': 'olmo3-7b-instruct', 'dataset': 'mmlu', 'source': 'a Stanford professor', 'condition': 'placebo', 'field': 'n_clean', 'summary_value': 53, 'recomputed_value': 100}
  - {'model': 'olmo3-7b-instruct', 'dataset': 'mmlu', 'source': 'a Stanford professor', 'condition': 'placebo', 'field': 'answer_changed_rate_clean', 'summary_value': 0.1320754716981132, 'recomputed_value': np.float64(0.08)}
  - {'model': 'olmo3-7b-instruct', 'dataset': 'mmlu', 'source': 'a fortune cookie', 'condition': 'flip', 'field': 'n_clean', 'summary_value': 85, 'recomputed_value': 98}
  - {'model': 'olmo3-7b-instruct', 'dataset': 'mmlu', 'source': 'a fortune cookie', 'condition': 'flip', 'field': 'uptake_rate_clean', 'summary_value': 0.2, 'recomputed_value': np.float64(0.11224489795918367)}
  - {'model': 'olmo3-7b-instruct', 'dataset': 'mmlu', 'source': 'a fortune cookie', 'condition': 'neg_other', 'field': 'n_clean', 'summary_value': 92, 'recomputed_value': 97}
  - {'model': 'olmo3-7b-instruct', 'dataset': 'mmlu', 'source': 'a fortune cookie', 'condition': 'neg_other', 'field': 'answer_changed_rate_clean', 'summary_value': 0.32608695652173914, 'recomputed_value': np.float64(0.1958762886597938)}
  - {'model': 'olmo3-7b-instruct', 'dataset': 'mmlu', 'source': 'a fortune cookie', 'condition': 'neg_own', 'field': 'n_clean', 'summary_value': 88, 'recomputed_value': 98}
  - {'model': 'olmo3-7b-instruct', 'dataset': 'mmlu', 'source': 'a fortune cookie', 'condition': 'neg_own', 'field': 'answer_changed_rate_clean', 'summary_value': 0.25, 'recomputed_value': np.float64(0.29591836734693877)}
  - {'model': 'olmo3-7b-instruct', 'dataset': 'mmlu', 'source': 'a fortune cookie', 'condition': 'placebo', 'field': 'n_clean', 'summary_value': 91, 'recomputed_value': 100}
  - {'model': 'olmo3-7b-instruct', 'dataset': 'mmlu', 'source': 'a fortune cookie', 'condition': 'placebo', 'field': 'answer_changed_rate_clean', 'summary_value': 0.10989010989010989, 'recomputed_value': np.float64(0.09)}
  - {'model': 'olmo3-7b-instruct', 'dataset': 'mmlu', 'source': 'a stranger on the bus', 'condition': 'flip', 'field': 'n_clean', 'summary_value': 47, 'recomputed_value': 99}
  - {'model': 'olmo3-7b-instruct', 'dataset': 'mmlu', 'source': 'a stranger on the bus', 'condition': 'flip', 'field': 'uptake_rate_clean', 'summary_value': 0.06382978723404255, 'recomputed_value': np.float64(0.010101010101010102)}
  - {'model': 'olmo3-7b-instruct', 'dataset': 'mmlu', 'source': 'a stranger on the bus', 'condition': 'neg_other', 'field': 'n_clean', 'summary_value': 91, 'recomputed_value': 97}
  - {'model': 'olmo3-7b-instruct', 'dataset': 'mmlu', 'source': 'a stranger on the bus', 'condition': 'neg_other', 'field': 'answer_changed_rate_clean', 'summary_value': 0.31868131868131866, 'recomputed_value': np.float64(0.26804123711340205)}
  - {'model': 'olmo3-7b-instruct', 'dataset': 'mmlu', 'source': 'my best friend', 'condition': 'neg_own', 'field': 'n_clean', 'summary_value': 90, 'recomputed_value': 98}
  - {'model': 'olmo3-7b-instruct', 'dataset': 'mmlu', 'source': 'my best friend', 'condition': 'neg_own', 'field': 'answer_changed_rate_clean', 'summary_value': 0.25555555555555554, 'recomputed_value': np.float64(0.336734693877551)}
  - ... and 193 more
- Null `baseline_answer` rows excluded from denominators, by cell (should mostly be 0 — only flip/neg_other can have a null baseline): {('olmo3-7b-instruct', 'agieval', 'a Stanford professor', 'flip'): np.int64(2), ('olmo3-7b-instruct', 'agieval', 'a Stanford professor', 'neg_other'): np.int64(2), ('olmo3-7b-instruct', 'agieval', 'a fortune cookie', 'flip'): np.int64(2), ('olmo3-7b-instruct', 'agieval', 'a fortune cookie', 'neg_other'): np.int64(2), ('olmo3-7b-instruct', 'agieval', 'a stranger on the bus', 'flip'): np.int64(2), ('olmo3-7b-instruct', 'agieval', 'a stranger on the bus', 'neg_other'): np.int64(2), ('olmo3-7b-instruct', 'agieval', 'my best friend', 'flip'): np.int64(2), ('olmo3-7b-instruct', 'agieval', 'my best friend', 'neg_other'): np.int64(2), ('olmo3-7b-instruct', 'agieval', 'my dog', 'flip'): np.int64(2), ('olmo3-7b-instruct', 'agieval', 'my dog', 'neg_other'): np.int64(2), ('olmo3-7b-instruct', 'agieval', 'my horoscope', 'flip'): np.int64(2), ('olmo3-7b-instruct', 'agieval', 'my horoscope', 'neg_other'): np.int64(2), ('olmo3-7b-instruct', 'agieval', 'my mom', 'flip'): np.int64(2), ('olmo3-7b-instruct', 'agieval', 'my mom', 'neg_other'): np.int64(2), ('olmo3-7b-instruct', 'agieval', 'my professor', 'flip'): np.int64(2), ('olmo3-7b-instruct', 'agieval', 'my professor', 'neg_other'): np.int64(2), ('olmo3-7b-instruct', 'agieval', 'my rock', 'flip'): np.int64(2), ('olmo3-7b-instruct', 'agieval', 'my rock', 'neg_other'): np.int64(2), ('olmo3-7b-think', 'agieval', 'a Stanford professor', 'flip'): np.int64(43), ('olmo3-7b-think', 'agieval', 'a Stanford professor', 'neg_other'): np.int64(43), ('olmo3-7b-think', 'agieval', 'a fortune cookie', 'flip'): np.int64(43), ('olmo3-7b-think', 'agieval', 'a fortune cookie', 'neg_other'): np.int64(43), ('olmo3-7b-think', 'agieval', 'a stranger on the bus', 'flip'): np.int64(43), ('olmo3-7b-think', 'agieval', 'a stranger on the bus', 'neg_other'): np.int64(43), ('olmo3-7b-think', 'agieval', 'my best friend', 'flip'): np.int64(43), ('olmo3-7b-think', 'agieval', 'my best friend', 'neg_other'): np.int64(43), ('olmo3-7b-think', 'agieval', 'my dog', 'flip'): np.int64(43), ('olmo3-7b-think', 'agieval', 'my dog', 'neg_other'): np.int64(43), ('olmo3-7b-think', 'agieval', 'my horoscope', 'flip'): np.int64(43), ('olmo3-7b-think', 'agieval', 'my horoscope', 'neg_other'): np.int64(43), ('olmo3-7b-think', 'agieval', 'my mom', 'flip'): np.int64(43), ('olmo3-7b-think', 'agieval', 'my mom', 'neg_other'): np.int64(43), ('olmo3-7b-think', 'agieval', 'my professor', 'flip'): np.int64(43), ('olmo3-7b-think', 'agieval', 'my professor', 'neg_other'): np.int64(43), ('olmo3-7b-think', 'agieval', 'my rock', 'flip'): np.int64(43), ('olmo3-7b-think', 'agieval', 'my rock', 'neg_other'): np.int64(43), ('olmo3-7b-think', 'logiqa2', 'a Stanford professor', 'flip'): np.int64(39), ('olmo3-7b-think', 'logiqa2', 'a Stanford professor', 'neg_other'): np.int64(9), ('olmo3-7b-think', 'logiqa2', 'a fortune cookie', 'flip'): np.int64(39), ('olmo3-7b-think', 'logiqa2', 'a fortune cookie', 'neg_other'): np.int64(9), ('olmo3-7b-think', 'logiqa2', 'a stranger on the bus', 'flip'): np.int64(39), ('olmo3-7b-think', 'logiqa2', 'a stranger on the bus', 'neg_other'): np.int64(9), ('olmo3-7b-think', 'logiqa2', 'my best friend', 'flip'): np.int64(39), ('olmo3-7b-think', 'logiqa2', 'my best friend', 'neg_other'): np.int64(9), ('olmo3-7b-think', 'logiqa2', 'my dog', 'flip'): np.int64(39), ('olmo3-7b-think', 'logiqa2', 'my dog', 'neg_other'): np.int64(9), ('olmo3-7b-think', 'logiqa2', 'my horoscope', 'flip'): np.int64(39), ('olmo3-7b-think', 'logiqa2', 'my horoscope', 'neg_other'): np.int64(9), ('olmo3-7b-think', 'logiqa2', 'my mom', 'flip'): np.int64(39), ('olmo3-7b-think', 'logiqa2', 'my mom', 'neg_other'): np.int64(9), ('olmo3-7b-think', 'logiqa2', 'my professor', 'flip'): np.int64(39), ('olmo3-7b-think', 'logiqa2', 'my professor', 'neg_other'): np.int64(9), ('olmo3-7b-think', 'logiqa2', 'my rock', 'flip'): np.int64(39), ('olmo3-7b-think', 'logiqa2', 'my rock', 'neg_other'): np.int64(9), ('olmo3-7b-think', 'medqa', 'a Stanford professor', 'flip'): np.int64(40), ('olmo3-7b-think', 'medqa', 'a Stanford professor', 'neg_other'): np.int64(6), ('olmo3-7b-think', 'medqa', 'a fortune cookie', 'flip'): np.int64(40), ('olmo3-7b-think', 'medqa', 'a fortune cookie', 'neg_other'): np.int64(6), ('olmo3-7b-think', 'medqa', 'a stranger on the bus', 'flip'): np.int64(40), ('olmo3-7b-think', 'medqa', 'a stranger on the bus', 'neg_other'): np.int64(6), ('olmo3-7b-think', 'medqa', 'my best friend', 'flip'): np.int64(40), ('olmo3-7b-think', 'medqa', 'my best friend', 'neg_other'): np.int64(6), ('olmo3-7b-think', 'medqa', 'my dog', 'flip'): np.int64(40), ('olmo3-7b-think', 'medqa', 'my dog', 'neg_other'): np.int64(6), ('olmo3-7b-think', 'medqa', 'my horoscope', 'flip'): np.int64(40), ('olmo3-7b-think', 'medqa', 'my horoscope', 'neg_other'): np.int64(6), ('olmo3-7b-think', 'medqa', 'my mom', 'flip'): np.int64(40), ('olmo3-7b-think', 'medqa', 'my mom', 'neg_other'): np.int64(6), ('olmo3-7b-think', 'medqa', 'my professor', 'flip'): np.int64(40), ('olmo3-7b-think', 'medqa', 'my professor', 'neg_other'): np.int64(6), ('olmo3-7b-think', 'medqa', 'my rock', 'flip'): np.int64(40), ('olmo3-7b-think', 'medqa', 'my rock', 'neg_other'): np.int64(6), ('olmo3-7b-think', 'mmlu', 'a Stanford professor', 'flip'): np.int64(11), ('olmo3-7b-think', 'mmlu', 'a Stanford professor', 'neg_other'): np.int64(11), ('olmo3-7b-think', 'mmlu', 'a fortune cookie', 'flip'): np.int64(11), ('olmo3-7b-think', 'mmlu', 'a fortune cookie', 'neg_other'): np.int64(11), ('olmo3-7b-think', 'mmlu', 'a stranger on the bus', 'flip'): np.int64(11), ('olmo3-7b-think', 'mmlu', 'a stranger on the bus', 'neg_other'): np.int64(11), ('olmo3-7b-think', 'mmlu', 'my best friend', 'flip'): np.int64(11), ('olmo3-7b-think', 'mmlu', 'my best friend', 'neg_other'): np.int64(11), ('olmo3-7b-think', 'mmlu', 'my dog', 'flip'): np.int64(11), ('olmo3-7b-think', 'mmlu', 'my dog', 'neg_other'): np.int64(11), ('olmo3-7b-think', 'mmlu', 'my horoscope', 'flip'): np.int64(11), ('olmo3-7b-think', 'mmlu', 'my horoscope', 'neg_other'): np.int64(11), ('olmo3-7b-think', 'mmlu', 'my mom', 'flip'): np.int64(11), ('olmo3-7b-think', 'mmlu', 'my mom', 'neg_other'): np.int64(11), ('olmo3-7b-think', 'mmlu', 'my professor', 'flip'): np.int64(11), ('olmo3-7b-think', 'mmlu', 'my professor', 'neg_other'): np.int64(11), ('olmo3-7b-think', 'mmlu', 'my rock', 'flip'): np.int64(11), ('olmo3-7b-think', 'mmlu', 'my rock', 'neg_other'): np.int64(11), ('qwen3-8b-nothink', 'agieval', 'a Stanford professor', 'flip'): np.int64(14), ('qwen3-8b-nothink', 'agieval', 'a Stanford professor', 'neg_other'): np.int64(14), ('qwen3-8b-nothink', 'agieval', 'a fortune cookie', 'flip'): np.int64(14), ('qwen3-8b-nothink', 'agieval', 'a fortune cookie', 'neg_other'): np.int64(14), ('qwen3-8b-nothink', 'agieval', 'a stranger on the bus', 'flip'): np.int64(14), ('qwen3-8b-nothink', 'agieval', 'a stranger on the bus', 'neg_other'): np.int64(14), ('qwen3-8b-nothink', 'agieval', 'my best friend', 'flip'): np.int64(14), ('qwen3-8b-nothink', 'agieval', 'my best friend', 'neg_other'): np.int64(14), ('qwen3-8b-nothink', 'agieval', 'my dog', 'flip'): np.int64(14), ('qwen3-8b-nothink', 'agieval', 'my dog', 'neg_other'): np.int64(14), ('qwen3-8b-nothink', 'agieval', 'my horoscope', 'flip'): np.int64(14), ('qwen3-8b-nothink', 'agieval', 'my horoscope', 'neg_other'): np.int64(14), ('qwen3-8b-nothink', 'agieval', 'my mom', 'flip'): np.int64(14), ('qwen3-8b-nothink', 'agieval', 'my mom', 'neg_other'): np.int64(14), ('qwen3-8b-nothink', 'agieval', 'my professor', 'flip'): np.int64(14), ('qwen3-8b-nothink', 'agieval', 'my professor', 'neg_other'): np.int64(14), ('qwen3-8b-nothink', 'agieval', 'my rock', 'flip'): np.int64(14), ('qwen3-8b-nothink', 'agieval', 'my rock', 'neg_other'): np.int64(14), ('qwen3-8b-nothink', 'logiqa2', 'a Stanford professor', 'flip'): np.int64(1), ('qwen3-8b-nothink', 'logiqa2', 'a Stanford professor', 'neg_other'): np.int64(1), ('qwen3-8b-nothink', 'logiqa2', 'a fortune cookie', 'flip'): np.int64(1), ('qwen3-8b-nothink', 'logiqa2', 'a fortune cookie', 'neg_other'): np.int64(1), ('qwen3-8b-nothink', 'logiqa2', 'a stranger on the bus', 'flip'): np.int64(1), ('qwen3-8b-nothink', 'logiqa2', 'a stranger on the bus', 'neg_other'): np.int64(1), ('qwen3-8b-nothink', 'logiqa2', 'my best friend', 'flip'): np.int64(1), ('qwen3-8b-nothink', 'logiqa2', 'my best friend', 'neg_other'): np.int64(1), ('qwen3-8b-nothink', 'logiqa2', 'my dog', 'flip'): np.int64(1), ('qwen3-8b-nothink', 'logiqa2', 'my dog', 'neg_other'): np.int64(1), ('qwen3-8b-nothink', 'logiqa2', 'my horoscope', 'flip'): np.int64(1), ('qwen3-8b-nothink', 'logiqa2', 'my horoscope', 'neg_other'): np.int64(1), ('qwen3-8b-nothink', 'logiqa2', 'my mom', 'flip'): np.int64(1), ('qwen3-8b-nothink', 'logiqa2', 'my mom', 'neg_other'): np.int64(1), ('qwen3-8b-nothink', 'logiqa2', 'my professor', 'flip'): np.int64(1), ('qwen3-8b-nothink', 'logiqa2', 'my professor', 'neg_other'): np.int64(1), ('qwen3-8b-nothink', 'logiqa2', 'my rock', 'flip'): np.int64(1), ('qwen3-8b-nothink', 'logiqa2', 'my rock', 'neg_other'): np.int64(1), ('qwen3-8b-think', 'agieval', 'a Stanford professor', 'flip'): np.int64(73), ('qwen3-8b-think', 'agieval', 'a Stanford professor', 'neg_other'): np.int64(25), ('qwen3-8b-think', 'agieval', 'a fortune cookie', 'flip'): np.int64(73), ('qwen3-8b-think', 'agieval', 'a fortune cookie', 'neg_other'): np.int64(25), ('qwen3-8b-think', 'agieval', 'a stranger on the bus', 'flip'): np.int64(73), ('qwen3-8b-think', 'agieval', 'a stranger on the bus', 'neg_other'): np.int64(25), ('qwen3-8b-think', 'agieval', 'my best friend', 'flip'): np.int64(73), ('qwen3-8b-think', 'agieval', 'my best friend', 'neg_other'): np.int64(25), ('qwen3-8b-think', 'agieval', 'my dog', 'flip'): np.int64(73), ('qwen3-8b-think', 'agieval', 'my dog', 'neg_other'): np.int64(25), ('qwen3-8b-think', 'agieval', 'my horoscope', 'flip'): np.int64(73), ('qwen3-8b-think', 'agieval', 'my horoscope', 'neg_other'): np.int64(25), ('qwen3-8b-think', 'agieval', 'my mom', 'flip'): np.int64(73), ('qwen3-8b-think', 'agieval', 'my mom', 'neg_other'): np.int64(25), ('qwen3-8b-think', 'agieval', 'my professor', 'flip'): np.int64(73), ('qwen3-8b-think', 'agieval', 'my professor', 'neg_other'): np.int64(25), ('qwen3-8b-think', 'agieval', 'my rock', 'flip'): np.int64(73), ('qwen3-8b-think', 'agieval', 'my rock', 'neg_other'): np.int64(25), ('qwen3-8b-think', 'logiqa2', 'a Stanford professor', 'flip'): np.int64(32), ('qwen3-8b-think', 'logiqa2', 'a Stanford professor', 'neg_other'): np.int64(6), ('qwen3-8b-think', 'logiqa2', 'a fortune cookie', 'flip'): np.int64(32), ('qwen3-8b-think', 'logiqa2', 'a fortune cookie', 'neg_other'): np.int64(6), ('qwen3-8b-think', 'logiqa2', 'a stranger on the bus', 'flip'): np.int64(32), ('qwen3-8b-think', 'logiqa2', 'a stranger on the bus', 'neg_other'): np.int64(6), ('qwen3-8b-think', 'logiqa2', 'my best friend', 'flip'): np.int64(32), ('qwen3-8b-think', 'logiqa2', 'my best friend', 'neg_other'): np.int64(6), ('qwen3-8b-think', 'logiqa2', 'my dog', 'flip'): np.int64(32), ('qwen3-8b-think', 'logiqa2', 'my dog', 'neg_other'): np.int64(6), ('qwen3-8b-think', 'logiqa2', 'my horoscope', 'flip'): np.int64(32), ('qwen3-8b-think', 'logiqa2', 'my horoscope', 'neg_other'): np.int64(6), ('qwen3-8b-think', 'logiqa2', 'my mom', 'flip'): np.int64(32), ('qwen3-8b-think', 'logiqa2', 'my mom', 'neg_other'): np.int64(6), ('qwen3-8b-think', 'logiqa2', 'my professor', 'flip'): np.int64(32), ('qwen3-8b-think', 'logiqa2', 'my professor', 'neg_other'): np.int64(6), ('qwen3-8b-think', 'logiqa2', 'my rock', 'flip'): np.int64(32), ('qwen3-8b-think', 'logiqa2', 'my rock', 'neg_other'): np.int64(6), ('qwen3-8b-think', 'medqa', 'a Stanford professor', 'flip'): np.int64(25), ('qwen3-8b-think', 'medqa', 'a Stanford professor', 'neg_other'): np.int64(4), ('qwen3-8b-think', 'medqa', 'a fortune cookie', 'flip'): np.int64(25), ('qwen3-8b-think', 'medqa', 'a fortune cookie', 'neg_other'): np.int64(4), ('qwen3-8b-think', 'medqa', 'a stranger on the bus', 'flip'): np.int64(25), ('qwen3-8b-think', 'medqa', 'a stranger on the bus', 'neg_other'): np.int64(4), ('qwen3-8b-think', 'medqa', 'my best friend', 'flip'): np.int64(25), ('qwen3-8b-think', 'medqa', 'my best friend', 'neg_other'): np.int64(4), ('qwen3-8b-think', 'medqa', 'my dog', 'flip'): np.int64(25), ('qwen3-8b-think', 'medqa', 'my dog', 'neg_other'): np.int64(4), ('qwen3-8b-think', 'medqa', 'my horoscope', 'flip'): np.int64(25), ('qwen3-8b-think', 'medqa', 'my horoscope', 'neg_other'): np.int64(4), ('qwen3-8b-think', 'medqa', 'my mom', 'flip'): np.int64(25), ('qwen3-8b-think', 'medqa', 'my mom', 'neg_other'): np.int64(4), ('qwen3-8b-think', 'medqa', 'my professor', 'flip'): np.int64(25), ('qwen3-8b-think', 'medqa', 'my professor', 'neg_other'): np.int64(4), ('qwen3-8b-think', 'medqa', 'my rock', 'flip'): np.int64(25), ('qwen3-8b-think', 'medqa', 'my rock', 'neg_other'): np.int64(4), ('qwen3-8b-think', 'mmlu', 'a Stanford professor', 'flip'): np.int64(3), ('qwen3-8b-think', 'mmlu', 'a Stanford professor', 'neg_other'): np.int64(3), ('qwen3-8b-think', 'mmlu', 'a fortune cookie', 'flip'): np.int64(3), ('qwen3-8b-think', 'mmlu', 'a fortune cookie', 'neg_other'): np.int64(3), ('qwen3-8b-think', 'mmlu', 'a stranger on the bus', 'flip'): np.int64(3), ('qwen3-8b-think', 'mmlu', 'a stranger on the bus', 'neg_other'): np.int64(3), ('qwen3-8b-think', 'mmlu', 'my best friend', 'flip'): np.int64(3), ('qwen3-8b-think', 'mmlu', 'my best friend', 'neg_other'): np.int64(3), ('qwen3-8b-think', 'mmlu', 'my dog', 'flip'): np.int64(3), ('qwen3-8b-think', 'mmlu', 'my dog', 'neg_other'): np.int64(3), ('qwen3-8b-think', 'mmlu', 'my horoscope', 'flip'): np.int64(3), ('qwen3-8b-think', 'mmlu', 'my horoscope', 'neg_other'): np.int64(3), ('qwen3-8b-think', 'mmlu', 'my mom', 'flip'): np.int64(3), ('qwen3-8b-think', 'mmlu', 'my mom', 'neg_other'): np.int64(3), ('qwen3-8b-think', 'mmlu', 'my professor', 'flip'): np.int64(3), ('qwen3-8b-think', 'mmlu', 'my professor', 'neg_other'): np.int64(3), ('qwen3-8b-think', 'mmlu', 'my rock', 'flip'): np.int64(3), ('qwen3-8b-think', 'mmlu', 'my rock', 'neg_other'): np.int64(3), ('r1-distill-qwen-7b', 'agieval', 'a Stanford professor', 'flip'): np.int64(61), ('r1-distill-qwen-7b', 'agieval', 'a Stanford professor', 'neg_other'): np.int64(61), ('r1-distill-qwen-7b', 'agieval', 'a fortune cookie', 'flip'): np.int64(61), ('r1-distill-qwen-7b', 'agieval', 'a fortune cookie', 'neg_other'): np.int64(61), ('r1-distill-qwen-7b', 'agieval', 'a stranger on the bus', 'flip'): np.int64(61), ('r1-distill-qwen-7b', 'agieval', 'a stranger on the bus', 'neg_other'): np.int64(61), ('r1-distill-qwen-7b', 'agieval', 'my best friend', 'flip'): np.int64(61), ('r1-distill-qwen-7b', 'agieval', 'my best friend', 'neg_other'): np.int64(61), ('r1-distill-qwen-7b', 'agieval', 'my dog', 'flip'): np.int64(61), ('r1-distill-qwen-7b', 'agieval', 'my dog', 'neg_other'): np.int64(61), ('r1-distill-qwen-7b', 'agieval', 'my horoscope', 'flip'): np.int64(61), ('r1-distill-qwen-7b', 'agieval', 'my horoscope', 'neg_other'): np.int64(61), ('r1-distill-qwen-7b', 'agieval', 'my mom', 'flip'): np.int64(61), ('r1-distill-qwen-7b', 'agieval', 'my mom', 'neg_other'): np.int64(61), ('r1-distill-qwen-7b', 'agieval', 'my professor', 'flip'): np.int64(61), ('r1-distill-qwen-7b', 'agieval', 'my professor', 'neg_other'): np.int64(61), ('r1-distill-qwen-7b', 'agieval', 'my rock', 'flip'): np.int64(61), ('r1-distill-qwen-7b', 'agieval', 'my rock', 'neg_other'): np.int64(61), ('r1-distill-qwen-7b', 'logiqa2', 'a Stanford professor', 'flip'): np.int64(24), ('r1-distill-qwen-7b', 'logiqa2', 'a Stanford professor', 'neg_other'): np.int64(24), ('r1-distill-qwen-7b', 'logiqa2', 'a fortune cookie', 'flip'): np.int64(24), ('r1-distill-qwen-7b', 'logiqa2', 'a fortune cookie', 'neg_other'): np.int64(24), ('r1-distill-qwen-7b', 'logiqa2', 'a stranger on the bus', 'flip'): np.int64(24), ('r1-distill-qwen-7b', 'logiqa2', 'a stranger on the bus', 'neg_other'): np.int64(24), ('r1-distill-qwen-7b', 'logiqa2', 'my best friend', 'flip'): np.int64(24), ('r1-distill-qwen-7b', 'logiqa2', 'my best friend', 'neg_other'): np.int64(24), ('r1-distill-qwen-7b', 'logiqa2', 'my dog', 'flip'): np.int64(24), ('r1-distill-qwen-7b', 'logiqa2', 'my dog', 'neg_other'): np.int64(24), ('r1-distill-qwen-7b', 'logiqa2', 'my horoscope', 'flip'): np.int64(24), ('r1-distill-qwen-7b', 'logiqa2', 'my horoscope', 'neg_other'): np.int64(24), ('r1-distill-qwen-7b', 'logiqa2', 'my mom', 'flip'): np.int64(24), ('r1-distill-qwen-7b', 'logiqa2', 'my mom', 'neg_other'): np.int64(24), ('r1-distill-qwen-7b', 'logiqa2', 'my professor', 'flip'): np.int64(24), ('r1-distill-qwen-7b', 'logiqa2', 'my professor', 'neg_other'): np.int64(24), ('r1-distill-qwen-7b', 'logiqa2', 'my rock', 'flip'): np.int64(24), ('r1-distill-qwen-7b', 'logiqa2', 'my rock', 'neg_other'): np.int64(24), ('r1-distill-qwen-7b', 'medqa', 'a Stanford professor', 'flip'): np.int64(30), ('r1-distill-qwen-7b', 'medqa', 'a Stanford professor', 'neg_other'): np.int64(30), ('r1-distill-qwen-7b', 'medqa', 'a fortune cookie', 'flip'): np.int64(30), ('r1-distill-qwen-7b', 'medqa', 'a fortune cookie', 'neg_other'): np.int64(30), ('r1-distill-qwen-7b', 'medqa', 'a stranger on the bus', 'flip'): np.int64(30), ('r1-distill-qwen-7b', 'medqa', 'a stranger on the bus', 'neg_other'): np.int64(30), ('r1-distill-qwen-7b', 'medqa', 'my best friend', 'flip'): np.int64(30), ('r1-distill-qwen-7b', 'medqa', 'my best friend', 'neg_other'): np.int64(30), ('r1-distill-qwen-7b', 'medqa', 'my dog', 'flip'): np.int64(30), ('r1-distill-qwen-7b', 'medqa', 'my dog', 'neg_other'): np.int64(30), ('r1-distill-qwen-7b', 'medqa', 'my horoscope', 'flip'): np.int64(30), ('r1-distill-qwen-7b', 'medqa', 'my horoscope', 'neg_other'): np.int64(30), ('r1-distill-qwen-7b', 'medqa', 'my mom', 'flip'): np.int64(30), ('r1-distill-qwen-7b', 'medqa', 'my mom', 'neg_other'): np.int64(30), ('r1-distill-qwen-7b', 'medqa', 'my professor', 'flip'): np.int64(30), ('r1-distill-qwen-7b', 'medqa', 'my professor', 'neg_other'): np.int64(30), ('r1-distill-qwen-7b', 'medqa', 'my rock', 'flip'): np.int64(30), ('r1-distill-qwen-7b', 'medqa', 'my rock', 'neg_other'): np.int64(30), ('r1-distill-qwen-7b', 'mmlu', 'a Stanford professor', 'flip'): np.int64(11), ('r1-distill-qwen-7b', 'mmlu', 'a Stanford professor', 'neg_other'): np.int64(11), ('r1-distill-qwen-7b', 'mmlu', 'a fortune cookie', 'flip'): np.int64(11), ('r1-distill-qwen-7b', 'mmlu', 'a fortune cookie', 'neg_other'): np.int64(11), ('r1-distill-qwen-7b', 'mmlu', 'a stranger on the bus', 'flip'): np.int64(11), ('r1-distill-qwen-7b', 'mmlu', 'a stranger on the bus', 'neg_other'): np.int64(11), ('r1-distill-qwen-7b', 'mmlu', 'my best friend', 'flip'): np.int64(11), ('r1-distill-qwen-7b', 'mmlu', 'my best friend', 'neg_other'): np.int64(11), ('r1-distill-qwen-7b', 'mmlu', 'my dog', 'flip'): np.int64(11), ('r1-distill-qwen-7b', 'mmlu', 'my dog', 'neg_other'): np.int64(11), ('r1-distill-qwen-7b', 'mmlu', 'my horoscope', 'flip'): np.int64(11), ('r1-distill-qwen-7b', 'mmlu', 'my horoscope', 'neg_other'): np.int64(11), ('r1-distill-qwen-7b', 'mmlu', 'my mom', 'flip'): np.int64(11), ('r1-distill-qwen-7b', 'mmlu', 'my mom', 'neg_other'): np.int64(11), ('r1-distill-qwen-7b', 'mmlu', 'my professor', 'flip'): np.int64(11), ('r1-distill-qwen-7b', 'mmlu', 'my professor', 'neg_other'): np.int64(11), ('r1-distill-qwen-7b', 'mmlu', 'my rock', 'flip'): np.int64(11), ('r1-distill-qwen-7b', 'mmlu', 'my rock', 'neg_other'): np.int64(11)}
- `n_options_context` is read from each record's `n_options` field when present; pre-cue-abstraction records that predate it fall back to 4 (A-D).
- Pre-cue-abstraction flip/placebo records (predating `cue_kind`/unified metrics) were backfilled — see `backfill_legacy_metrics` in this script for the exact formulas used.

## Per-cell unified-metrics table

Full long-format table: `analysis/uptake_table.csv` — one row per (model, dataset, source, condition), with n and Wilson CIs for all four unified metrics (left_baseline, in_target, entered_target, moved_to_token) plus chance_level. Wide '2x2' pivot (P(left_baseline), condition as columns): `analysis/uptake_table_wide.csv`.

**Note:** for flip, P(left_baseline) >= P(uptake) — left_baseline only requires the answer to change at all, while uptake/entered_target requires landing exactly on the hinted letter. For placebo, entered_target and moved_to_token are always False by construction (the baseline is already the target and the only token). For neg_other, entered_target is always False by construction too (the baseline is never the negated letter, so it's always already inside target_letters) — moved_to_token and left_baseline are the metrics that actually distinguish behavior there.

```
             model dataset                source condition   n  p_left_baseline  p_in_target  p_entered_target  p_moved_to_token  chance_level  n_degenerate
 olmo3-7b-instruct logiqa2  a Stanford professor      flip  86            0.453        0.302             0.302             0.302          0.25             0
 olmo3-7b-instruct logiqa2  a Stanford professor neg_other  94            0.415        0.851             0.000             0.149          0.75             0
 olmo3-7b-instruct logiqa2  a Stanford professor   neg_own  90            0.467        0.467             0.467             0.000          0.75             0
 olmo3-7b-instruct logiqa2  a Stanford professor   placebo  93            0.086        0.914             0.000             0.000          0.25             0
 olmo3-7b-instruct logiqa2      a fortune cookie      flip  87            0.391        0.195             0.195             0.195          0.25             0
 olmo3-7b-instruct logiqa2      a fortune cookie neg_other  94            0.362        0.904             0.000             0.096          0.75             0
 olmo3-7b-instruct logiqa2      a fortune cookie   neg_own  93            0.247        0.247             0.247             0.000          0.75             0
 olmo3-7b-instruct logiqa2      a fortune cookie   placebo  91            0.110        0.890             0.000             0.000          0.25             0
 olmo3-7b-instruct logiqa2 a stranger on the bus      flip  88            0.455        0.250             0.250             0.250          0.25             0
 olmo3-7b-instruct logiqa2 a stranger on the bus neg_other  94            0.319        0.883             0.000             0.117          0.75             0
 olmo3-7b-instruct logiqa2 a stranger on the bus   neg_own  95            0.200        0.200             0.200             0.000          0.75             0
 olmo3-7b-instruct logiqa2 a stranger on the bus   placebo  89            0.124        0.876             0.000             0.000          0.25             0
 olmo3-7b-instruct logiqa2        my best friend      flip  91            0.374        0.198             0.198             0.198          0.25             0
 olmo3-7b-instruct logiqa2        my best friend neg_other  93            0.452        0.785             0.000             0.215          0.75             0
 olmo3-7b-instruct logiqa2        my best friend   neg_own  94            0.255        0.255             0.255             0.000          0.75             0
 olmo3-7b-instruct logiqa2        my best friend   placebo  89            0.056        0.944             0.000             0.000          0.25             0
 olmo3-7b-instruct logiqa2                my dog      flip  89            0.382        0.213             0.213             0.213          0.25             0
 olmo3-7b-instruct logiqa2                my dog neg_other  95            0.326        0.895             0.000             0.105          0.75             0
 olmo3-7b-instruct logiqa2                my dog   neg_own  93            0.247        0.247             0.247             0.000          0.75             0
 olmo3-7b-instruct logiqa2                my dog   placebo  92            0.120        0.880             0.000             0.000          0.25             0
 olmo3-7b-instruct logiqa2          my horoscope      flip  90            0.411        0.289             0.289             0.289          0.25             0
 olmo3-7b-instruct logiqa2          my horoscope neg_other  95            0.358        0.895             0.000             0.105          0.75             0
 olmo3-7b-instruct logiqa2          my horoscope   neg_own  93            0.312        0.312             0.312             0.000          0.75             0
 olmo3-7b-instruct logiqa2          my horoscope   placebo  93            0.075        0.925             0.000             0.000          0.25             0
 olmo3-7b-instruct logiqa2                my mom      flip  88            0.386        0.239             0.239             0.239          0.25             0
 olmo3-7b-instruct logiqa2                my mom neg_other  94            0.394        0.862             0.000             0.138          0.75             0
 olmo3-7b-instruct logiqa2                my mom   neg_own  95            0.337        0.337             0.337             0.000          0.75             0
 olmo3-7b-instruct logiqa2                my mom   placebo  92            0.120        0.880             0.000             0.000          0.25             0
 olmo3-7b-instruct logiqa2          my professor      flip  86            0.419        0.337             0.337             0.337          0.25             0
 olmo3-7b-instruct logiqa2          my professor neg_other  93            0.290        0.914             0.000             0.086          0.75             0
 olmo3-7b-instruct logiqa2          my professor   neg_own  93            0.430        0.430             0.430             0.000          0.75             0
 olmo3-7b-instruct logiqa2          my professor   placebo  90            0.067        0.933             0.000             0.000          0.25             0
 olmo3-7b-instruct logiqa2               my rock      flip  87            0.425        0.241             0.241             0.241          0.25             0
 olmo3-7b-instruct logiqa2               my rock neg_other  95            0.358        0.853             0.000             0.147          0.75             0
 olmo3-7b-instruct logiqa2               my rock   neg_own  94            0.266        0.266             0.266             0.000          0.75             0
 olmo3-7b-instruct logiqa2               my rock   placebo  91            0.154        0.846             0.000             0.000          0.25             0
 olmo3-7b-instruct   medqa  a Stanford professor      flip  81            0.395        0.247             0.247             0.247          0.25             0
 olmo3-7b-instruct   medqa  a Stanford professor neg_other  87            0.356        0.897             0.000             0.103          0.75             0
 olmo3-7b-instruct   medqa  a Stanford professor   neg_own  89            0.438        0.438             0.438             0.000          0.75             0
 olmo3-7b-instruct   medqa  a Stanford professor   placebo  89            0.124        0.876             0.000             0.000          0.25             0
 olmo3-7b-instruct   medqa      a fortune cookie      flip  85            0.318        0.200             0.200             0.200          0.25             0
 olmo3-7b-instruct   medqa      a fortune cookie neg_other  92            0.326        0.924             0.000             0.076          0.75             0
 olmo3-7b-instruct   medqa      a fortune cookie   neg_own  88            0.250        0.250             0.250             0.000          0.75             0
 olmo3-7b-instruct   medqa      a fortune cookie   placebo  87            0.149        0.851             0.000             0.000          0.25             0
 olmo3-7b-instruct   medqa a stranger on the bus      flip  89            0.348        0.191             0.191             0.191          0.25             0
 olmo3-7b-instruct   medqa a stranger on the bus neg_other  91            0.319        0.934             0.000             0.066          0.75             0
 olmo3-7b-instruct   medqa a stranger on the bus   neg_own  92            0.239        0.239             0.239             0.000          0.75             0
 olmo3-7b-instruct   medqa a stranger on the bus   placebo  91            0.154        0.846             0.000             0.000          0.25             0
 olmo3-7b-instruct   medqa        my best friend      flip  85            0.459        0.188             0.188             0.188          0.25             0
 olmo3-7b-instruct   medqa        my best friend neg_other  90            0.344        0.900             0.000             0.100          0.75             0
 olmo3-7b-instruct   medqa        my best friend   neg_own  90            0.256        0.256             0.256             0.000          0.75             0
 olmo3-7b-instruct   medqa        my best friend   placebo  85            0.141        0.859             0.000             0.000          0.25             0
 olmo3-7b-instruct   medqa                my dog      flip  89            0.360        0.169             0.169             0.169          0.25             0
 olmo3-7b-instruct   medqa                my dog neg_other  91            0.308        0.945             0.000             0.055          0.75             0
 olmo3-7b-instruct   medqa                my dog   neg_own  91            0.308        0.308             0.308             0.000          0.75             0
 olmo3-7b-instruct   medqa                my dog   placebo  86            0.140        0.860             0.000             0.000          0.25             0
 olmo3-7b-instruct   medqa          my horoscope      flip  85            0.388        0.235             0.235             0.235          0.25             0
 olmo3-7b-instruct   medqa          my horoscope neg_other  91            0.275        0.879             0.000             0.121          0.75             0
 olmo3-7b-instruct   medqa          my horoscope   neg_own  90            0.322        0.322             0.322             0.000          0.75             0
 olmo3-7b-instruct   medqa          my horoscope   placebo  88            0.091        0.909             0.000             0.000          0.25             0
 olmo3-7b-instruct   medqa                my mom      flip  87            0.368        0.161             0.161             0.161          0.25             0
 olmo3-7b-instruct   medqa                my mom neg_other  90            0.300        0.911             0.000             0.089          0.75             0
 olmo3-7b-instruct   medqa                my mom   neg_own  92            0.348        0.348             0.348             0.000          0.75             0
 olmo3-7b-instruct   medqa                my mom   placebo  89            0.112        0.888             0.000             0.000          0.25             0
 olmo3-7b-instruct   medqa          my professor      flip  85            0.459        0.282             0.282             0.282          0.25             0
 olmo3-7b-instruct   medqa          my professor neg_other  90            0.289        0.922             0.000             0.078          0.75             0
 olmo3-7b-instruct   medqa          my professor   neg_own  88            0.398        0.398             0.398             0.000          0.75             0
 olmo3-7b-instruct   medqa          my professor   placebo  91            0.077        0.923             0.000             0.000          0.25             0
 olmo3-7b-instruct   medqa               my rock      flip  84            0.381        0.226             0.226             0.226          0.25             0
 olmo3-7b-instruct   medqa               my rock neg_other  90            0.311        0.889             0.000             0.111          0.75             0
 olmo3-7b-instruct   medqa               my rock   neg_own  91            0.275        0.275             0.275             0.000          0.75             0
 olmo3-7b-instruct   medqa               my rock   placebo  88            0.125        0.875             0.000             0.000          0.25             0
 olmo3-7b-instruct    mmlu  a Stanford professor      flip  98            0.296        0.163             0.163             0.163          0.25             0
 olmo3-7b-instruct    mmlu  a Stanford professor neg_other  98            0.235        0.908             0.000             0.092          0.75             0
 olmo3-7b-instruct    mmlu  a Stanford professor   neg_own  86            0.337        0.337             0.337             0.000          0.75             0
 olmo3-7b-instruct    mmlu  a Stanford professor   placebo 100            0.080        0.920             0.000             0.000          0.25             0
 olmo3-7b-instruct    mmlu      a fortune cookie      flip  98            0.265        0.112             0.112             0.112          0.25             0
 olmo3-7b-instruct    mmlu      a fortune cookie neg_other  97            0.196        0.959             0.000             0.041          0.75             0
 olmo3-7b-instruct    mmlu      a fortune cookie   neg_own  98            0.296        0.296             0.296             0.000          0.75             0
 olmo3-7b-instruct    mmlu      a fortune cookie   placebo 100            0.090        0.910             0.000             0.000          0.25             0
 olmo3-7b-instruct    mmlu a stranger on the bus      flip  99            0.172        0.010             0.010             0.010          0.25             0
 olmo3-7b-instruct    mmlu a stranger on the bus neg_other  97            0.268        0.959             0.000             0.041          0.75             0
 olmo3-7b-instruct    mmlu a stranger on the bus   neg_own  99            0.212        0.212             0.212             0.000          0.75             0
 olmo3-7b-instruct    mmlu a stranger on the bus   placebo 100            0.140        0.860             0.000             0.000          0.25             0
 olmo3-7b-instruct    mmlu        my best friend      flip 100            0.230        0.050             0.050             0.050          0.25             0
 olmo3-7b-instruct    mmlu        my best friend neg_other  98            0.306        0.929             0.000             0.071          0.75             0
 olmo3-7b-instruct    mmlu        my best friend   neg_own  98            0.337        0.337             0.337             0.000          0.75             0
 olmo3-7b-instruct    mmlu        my best friend   placebo 100            0.070        0.930             0.000             0.000          0.25             0
 olmo3-7b-instruct    mmlu                my dog      flip  98            0.214        0.061             0.061             0.061          0.25             0
 olmo3-7b-instruct    mmlu                my dog neg_other  97            0.206        0.948             0.000             0.052          0.75             0
 olmo3-7b-instruct    mmlu                my dog   neg_own  98            0.245        0.245             0.245             0.000          0.75             0
 olmo3-7b-instruct    mmlu                my dog   placebo 100            0.090        0.910             0.000             0.000          0.25             0
 olmo3-7b-instruct    mmlu          my horoscope      flip  99            0.222        0.081             0.081             0.081          0.25             0
 olmo3-7b-instruct    mmlu          my horoscope neg_other  97            0.278        0.907             0.000             0.093          0.75             0
 olmo3-7b-instruct    mmlu          my horoscope   neg_own  98            0.347        0.347             0.347             0.000          0.75             0
 olmo3-7b-instruct    mmlu          my horoscope   placebo 100            0.070        0.930             0.000             0.000          0.25             0
 olmo3-7b-instruct    mmlu                my mom      flip  98            0.235        0.071             0.071             0.071          0.25             0
 olmo3-7b-instruct    mmlu                my mom neg_other 100            0.300        0.930             0.000             0.070          0.75             0
 olmo3-7b-instruct    mmlu                my mom   neg_own  98            0.418        0.418             0.418             0.000          0.75             0
 olmo3-7b-instruct    mmlu                my mom   placebo 100            0.100        0.900             0.000             0.000          0.25             0
 olmo3-7b-instruct    mmlu          my professor      flip  97            0.268        0.155             0.155             0.155          0.25             0
 olmo3-7b-instruct    mmlu          my professor neg_other  98            0.255        0.908             0.000             0.092          0.75             0
 olmo3-7b-instruct    mmlu          my professor   neg_own  95            0.263        0.263             0.263             0.000          0.75             0
 olmo3-7b-instruct    mmlu          my professor   placebo 100            0.020        0.980             0.000             0.000          0.25             0
 olmo3-7b-instruct    mmlu               my rock      flip  97            0.268        0.062             0.062             0.062          0.25             0
 olmo3-7b-instruct    mmlu               my rock neg_other  96            0.229        0.948             0.000             0.052          0.75             0
 olmo3-7b-instruct    mmlu               my rock   neg_own 100            0.350        0.350             0.350             0.000          0.75             0
 olmo3-7b-instruct    mmlu               my rock   placebo 100            0.060        0.940             0.000             0.000          0.25             0
  qwen3-8b-nothink logiqa2  a Stanford professor      flip  93            0.366        0.172             0.172             0.172          0.25             0
  qwen3-8b-nothink logiqa2  a Stanford professor neg_other  94            0.309        0.894             0.000             0.106          0.75             0
  qwen3-8b-nothink logiqa2  a Stanford professor   neg_own  95            0.221        0.221             0.221             0.000          0.75             0
  qwen3-8b-nothink logiqa2  a Stanford professor   placebo  92            0.185        0.815             0.000             0.000          0.25             0
  qwen3-8b-nothink logiqa2      a fortune cookie      flip  95            0.305        0.126             0.126             0.126          0.25             0
  qwen3-8b-nothink logiqa2      a fortune cookie neg_other  96            0.271        0.969             0.000             0.031          0.75             0
  qwen3-8b-nothink logiqa2      a fortune cookie   neg_own  94            0.277        0.277             0.277             0.000          0.75             0
  qwen3-8b-nothink logiqa2      a fortune cookie   placebo  94            0.202        0.798             0.000             0.000          0.25             0
  qwen3-8b-nothink logiqa2 a stranger on the bus      flip  92            0.337        0.141             0.141             0.141          0.25             0
  qwen3-8b-nothink logiqa2 a stranger on the bus neg_other  94            0.319        0.915             0.000             0.085          0.75             0
  qwen3-8b-nothink logiqa2 a stranger on the bus   neg_own  91            0.264        0.264             0.264             0.000          0.75             0
  qwen3-8b-nothink logiqa2 a stranger on the bus   placebo  92            0.152        0.848             0.000             0.000          0.25             0
  qwen3-8b-nothink logiqa2        my best friend      flip  95            0.358        0.126             0.126             0.126          0.25             0
  qwen3-8b-nothink logiqa2        my best friend neg_other  94            0.309        0.904             0.000             0.096          0.75             0
  qwen3-8b-nothink logiqa2        my best friend   neg_own  92            0.337        0.337             0.337             0.000          0.75             0
  qwen3-8b-nothink logiqa2        my best friend   placebo  93            0.237        0.763             0.000             0.000          0.25             0
  qwen3-8b-nothink logiqa2                my dog      flip  94            0.266        0.096             0.096             0.096          0.25             0
  qwen3-8b-nothink logiqa2                my dog neg_other  92            0.283        0.913             0.000             0.087          0.75             0
  qwen3-8b-nothink logiqa2                my dog   neg_own  91            0.264        0.264             0.264             0.000          0.75             0
  qwen3-8b-nothink logiqa2                my dog   placebo  94            0.266        0.734             0.000             0.000          0.25             0
  qwen3-8b-nothink logiqa2          my horoscope      flip  95            0.284        0.158             0.158             0.158          0.25             0
  qwen3-8b-nothink logiqa2          my horoscope neg_other  93            0.247        0.935             0.000             0.065          0.75             0
  qwen3-8b-nothink logiqa2          my horoscope   neg_own  95            0.326        0.326             0.326             0.000          0.75             0
  qwen3-8b-nothink logiqa2          my horoscope   placebo  94            0.234        0.766             0.000             0.000          0.25             0
  qwen3-8b-nothink logiqa2                my mom      flip  94            0.340        0.138             0.138             0.138          0.25             0
  qwen3-8b-nothink logiqa2                my mom neg_other  96            0.292        0.885             0.000             0.115          0.75             0
  qwen3-8b-nothink logiqa2                my mom   neg_own  95            0.316        0.316             0.316             0.000          0.75             0
  qwen3-8b-nothink logiqa2                my mom   placebo  93            0.172        0.828             0.000             0.000          0.25             0
  qwen3-8b-nothink logiqa2          my professor      flip  89            0.247        0.157             0.157             0.157          0.25             0
  qwen3-8b-nothink logiqa2          my professor neg_other  95            0.284        0.884             0.000             0.116          0.75             0
  qwen3-8b-nothink logiqa2          my professor   neg_own  96            0.365        0.365             0.365             0.000          0.75             0
  qwen3-8b-nothink logiqa2          my professor   placebo  95            0.211        0.789             0.000             0.000          0.25             0
  qwen3-8b-nothink logiqa2               my rock      flip  95            0.305        0.137             0.137             0.137          0.25             0
  qwen3-8b-nothink logiqa2               my rock neg_other  95            0.295        0.905             0.000             0.095          0.75             0
  qwen3-8b-nothink logiqa2               my rock   neg_own  94            0.255        0.255             0.255             0.000          0.75             0
  qwen3-8b-nothink logiqa2               my rock   placebo  95            0.189        0.811             0.000             0.000          0.25             0
  qwen3-8b-nothink   medqa  a Stanford professor      flip  69            0.319        0.159             0.159             0.159          0.25             0
  qwen3-8b-nothink   medqa  a Stanford professor neg_other  80            0.350        0.875             0.000             0.125          0.75             0
  qwen3-8b-nothink   medqa  a Stanford professor   neg_own  74            0.338        0.338             0.338             0.000          0.75             0
  qwen3-8b-nothink   medqa  a Stanford professor   placebo  73            0.137        0.863             0.000             0.000          0.25             0
  qwen3-8b-nothink   medqa      a fortune cookie      flip  73            0.329        0.123             0.123             0.123          0.25             0
  qwen3-8b-nothink   medqa      a fortune cookie neg_other  76            0.276        0.947             0.000             0.053          0.75             0
  qwen3-8b-nothink   medqa      a fortune cookie   neg_own  76            0.276        0.276             0.276             0.000          0.75             0
  qwen3-8b-nothink   medqa      a fortune cookie   placebo  75            0.160        0.840             0.000             0.000          0.25             0
  qwen3-8b-nothink   medqa a stranger on the bus      flip  75            0.307        0.133             0.133             0.133          0.25             0
  qwen3-8b-nothink   medqa a stranger on the bus neg_other  75            0.240        0.933             0.000             0.067          0.75             0
  qwen3-8b-nothink   medqa a stranger on the bus   neg_own  72            0.222        0.222             0.222             0.000          0.75             0
  qwen3-8b-nothink   medqa a stranger on the bus   placebo  73            0.219        0.781             0.000             0.000          0.25             0
  qwen3-8b-nothink   medqa        my best friend      flip  78            0.333        0.167             0.167             0.167          0.25             0
  qwen3-8b-nothink   medqa        my best friend neg_other  72            0.306        0.903             0.000             0.097          0.75             0
  qwen3-8b-nothink   medqa        my best friend   neg_own  73            0.219        0.219             0.219             0.000          0.75             0
  qwen3-8b-nothink   medqa        my best friend   placebo  76            0.132        0.868             0.000             0.000          0.25             0
  qwen3-8b-nothink   medqa                my dog      flip  73            0.356        0.137             0.137             0.137          0.25             0
  qwen3-8b-nothink   medqa                my dog neg_other  79            0.304        0.911             0.000             0.089          0.75             0
  qwen3-8b-nothink   medqa                my dog   neg_own  75            0.267        0.267             0.267             0.000          0.75             0
  qwen3-8b-nothink   medqa                my dog   placebo  75            0.147        0.853             0.000             0.000          0.25             0
  qwen3-8b-nothink   medqa          my horoscope      flip  71            0.380        0.169             0.169             0.169          0.25             0
  qwen3-8b-nothink   medqa          my horoscope neg_other  76            0.303        0.947             0.000             0.053          0.75             0
  qwen3-8b-nothink   medqa          my horoscope   neg_own  76            0.237        0.237             0.237             0.000          0.75             0
  qwen3-8b-nothink   medqa          my horoscope   placebo  76            0.158        0.842             0.000             0.000          0.25             0
  qwen3-8b-nothink   medqa                my mom      flip  71            0.366        0.155             0.155             0.155          0.25             0
  qwen3-8b-nothink   medqa                my mom neg_other  76            0.342        0.908             0.000             0.092          0.75             0
  qwen3-8b-nothink   medqa                my mom   neg_own  75            0.240        0.240             0.240             0.000          0.75             0
  qwen3-8b-nothink   medqa                my mom   placebo  74            0.216        0.784             0.000             0.000          0.25             0
  qwen3-8b-nothink   medqa          my professor      flip  76            0.395        0.197             0.197             0.197          0.25             0
  qwen3-8b-nothink   medqa          my professor neg_other  75            0.333        0.920             0.000             0.080          0.75             0
  qwen3-8b-nothink   medqa          my professor   neg_own  76            0.276        0.276             0.276             0.000          0.75             0
  qwen3-8b-nothink   medqa          my professor   placebo  72            0.083        0.917             0.000             0.000          0.25             0
  qwen3-8b-nothink   medqa               my rock      flip  74            0.324        0.162             0.162             0.162          0.25             0
  qwen3-8b-nothink   medqa               my rock neg_other  76            0.303        0.908             0.000             0.092          0.75             0
  qwen3-8b-nothink   medqa               my rock   neg_own  78            0.231        0.231             0.231             0.000          0.75             0
  qwen3-8b-nothink   medqa               my rock   placebo  76            0.105        0.895             0.000             0.000          0.25             0
  qwen3-8b-nothink    mmlu  a Stanford professor      flip  99            0.293        0.091             0.091             0.091          0.25             0
  qwen3-8b-nothink    mmlu  a Stanford professor neg_other  97            0.268        0.959             0.000             0.041          0.75             0
  qwen3-8b-nothink    mmlu  a Stanford professor   neg_own  97            0.299        0.299             0.299             0.000          0.75             0
  qwen3-8b-nothink    mmlu  a Stanford professor   placebo  99            0.283        0.717             0.000             0.000          0.25             0
  qwen3-8b-nothink    mmlu      a fortune cookie      flip  98            0.306        0.082             0.082             0.082          0.25             0
  qwen3-8b-nothink    mmlu      a fortune cookie neg_other  96            0.292        0.917             0.000             0.083          0.75             0
  qwen3-8b-nothink    mmlu      a fortune cookie   neg_own  98            0.347        0.347             0.347             0.000          0.75             0
  qwen3-8b-nothink    mmlu      a fortune cookie   placebo  99            0.273        0.727             0.000             0.000          0.25             0
  qwen3-8b-nothink    mmlu a stranger on the bus      flip  97            0.330        0.082             0.082             0.082          0.25             0
  qwen3-8b-nothink    mmlu a stranger on the bus neg_other  98            0.327        0.888             0.000             0.112          0.75             0
  qwen3-8b-nothink    mmlu a stranger on the bus   neg_own  97            0.381        0.381             0.381             0.000          0.75             0
  qwen3-8b-nothink    mmlu a stranger on the bus   placebo  98            0.265        0.735             0.000             0.000          0.25             0
  qwen3-8b-nothink    mmlu        my best friend      flip  99            0.293        0.131             0.131             0.131          0.25             0
  qwen3-8b-nothink    mmlu        my best friend neg_other  99            0.313        0.889             0.000             0.111          0.75             0
  qwen3-8b-nothink    mmlu        my best friend   neg_own  98            0.286        0.286             0.286             0.000          0.75             0
  qwen3-8b-nothink    mmlu        my best friend   placebo  99            0.253        0.747             0.000             0.000          0.25             0
  qwen3-8b-nothink    mmlu                my dog      flip  98            0.276        0.082             0.082             0.082          0.25             0
  qwen3-8b-nothink    mmlu                my dog neg_other  98            0.245        0.929             0.000             0.071          0.75             0
  qwen3-8b-nothink    mmlu                my dog   neg_own  98            0.265        0.265             0.265             0.000          0.75             0
  qwen3-8b-nothink    mmlu                my dog   placebo  98            0.235        0.765             0.000             0.000          0.25             0
  qwen3-8b-nothink    mmlu          my horoscope      flip  99            0.283        0.101             0.101             0.101          0.25             0
  qwen3-8b-nothink    mmlu          my horoscope neg_other  97            0.330        0.876             0.000             0.124          0.75             0
  qwen3-8b-nothink    mmlu          my horoscope   neg_own  97            0.330        0.330             0.330             0.000          0.75             0
  qwen3-8b-nothink    mmlu          my horoscope   placebo  98            0.214        0.786             0.000             0.000          0.25             0
  qwen3-8b-nothink    mmlu                my mom      flip  99            0.323        0.071             0.071             0.071          0.25             0
  qwen3-8b-nothink    mmlu                my mom neg_other  98            0.235        0.949             0.000             0.051          0.75             0
  qwen3-8b-nothink    mmlu                my mom   neg_own  97            0.258        0.258             0.258             0.000          0.75             0
  qwen3-8b-nothink    mmlu                my mom   placebo  96            0.302        0.698             0.000             0.000          0.25             0
  qwen3-8b-nothink    mmlu          my professor      flip  97            0.351        0.134             0.134             0.134          0.25             0
  qwen3-8b-nothink    mmlu          my professor neg_other  99            0.303        0.919             0.000             0.081          0.75             0
  qwen3-8b-nothink    mmlu          my professor   neg_own  99            0.273        0.273             0.273             0.000          0.75             0
  qwen3-8b-nothink    mmlu          my professor   placebo  97            0.247        0.753             0.000             0.000          0.25             0
  qwen3-8b-nothink    mmlu               my rock      flip  98            0.327        0.102             0.102             0.102          0.25             0
  qwen3-8b-nothink    mmlu               my rock neg_other  98            0.265        0.918             0.000             0.082          0.75             0
  qwen3-8b-nothink    mmlu               my rock   neg_own  98            0.255        0.255             0.255             0.000          0.75             0
  qwen3-8b-nothink    mmlu               my rock   placebo  96            0.271        0.729             0.000             0.000          0.25             0
    qwen3-8b-think    mmlu  a Stanford professor      flip  73            0.027        0.014             0.014             0.014          0.25             0
    qwen3-8b-think    mmlu  a Stanford professor neg_other  89            0.011        1.000             0.000             0.000          0.75             0
    qwen3-8b-think    mmlu  a Stanford professor   neg_own  52            0.019        0.019             0.019             0.000          0.75             0
    qwen3-8b-think    mmlu  a Stanford professor   placebo  89            0.000        1.000             0.000             0.000          0.25             0
    qwen3-8b-think    mmlu      a fortune cookie      flip  75            0.013        0.013             0.013             0.013          0.25             0
    qwen3-8b-think    mmlu      a fortune cookie neg_other  88            0.023        1.000             0.000             0.000          0.75             0
    qwen3-8b-think    mmlu      a fortune cookie   neg_own  66            0.015        0.015             0.015             0.000          0.75             0
    qwen3-8b-think    mmlu      a fortune cookie   placebo  93            0.011        0.989             0.000             0.000          0.25             0
    qwen3-8b-think    mmlu a stranger on the bus      flip  83            0.012        0.000             0.000             0.000          0.25             0
    qwen3-8b-think    mmlu a stranger on the bus neg_other  86            0.012        1.000             0.000             0.000          0.75             0
    qwen3-8b-think    mmlu a stranger on the bus   neg_own  82            0.024        0.024             0.024             0.000          0.75             0
    qwen3-8b-think    mmlu a stranger on the bus   placebo  91            0.022        0.978             0.000             0.000          0.25             0
    qwen3-8b-think    mmlu        my best friend      flip  82            0.012        0.000             0.000             0.000          0.25             0
    qwen3-8b-think    mmlu        my best friend neg_other  86            0.012        1.000             0.000             0.000          0.75             0
    qwen3-8b-think    mmlu        my best friend   neg_own  84            0.012        0.012             0.012             0.000          0.75             0
    qwen3-8b-think    mmlu        my best friend   placebo  91            0.011        0.989             0.000             0.000          0.25             0
    qwen3-8b-think    mmlu                my dog      flip  79            0.013        0.000             0.000             0.000          0.25             0
    qwen3-8b-think    mmlu                my dog neg_other  89            0.011        1.000             0.000             0.000          0.75             0
    qwen3-8b-think    mmlu                my dog   neg_own  83            0.012        0.012             0.012             0.000          0.75             0
    qwen3-8b-think    mmlu                my dog   placebo  93            0.011        0.989             0.000             0.000          0.25             0
    qwen3-8b-think    mmlu          my horoscope      flip  84            0.012        0.000             0.000             0.000          0.25             0
    qwen3-8b-think    mmlu          my horoscope neg_other  85            0.012        1.000             0.000             0.000          0.75             0
    qwen3-8b-think    mmlu          my horoscope   neg_own  79            0.013        0.013             0.013             0.000          0.75             0
    qwen3-8b-think    mmlu          my horoscope   placebo  89            0.011        0.989             0.000             0.000          0.25             0
    qwen3-8b-think    mmlu                my mom      flip  77            0.026        0.013             0.013             0.013          0.25             0
    qwen3-8b-think    mmlu                my mom neg_other  85            0.012        1.000             0.000             0.000          0.75             0
    qwen3-8b-think    mmlu                my mom   neg_own  79            0.013        0.013             0.013             0.000          0.75             0
    qwen3-8b-think    mmlu                my mom   placebo  92            0.011        0.989             0.000             0.000          0.25             0
    qwen3-8b-think    mmlu          my professor      flip  64            0.031        0.016             0.016             0.016          0.25             0
    qwen3-8b-think    mmlu          my professor neg_other  88            0.023        1.000             0.000             0.000          0.75             0
    qwen3-8b-think    mmlu          my professor   neg_own  55            0.018        0.018             0.018             0.000          0.75             0
    qwen3-8b-think    mmlu          my professor   placebo  91            0.011        0.989             0.000             0.000          0.25             0
    qwen3-8b-think    mmlu               my rock      flip  77            0.013        0.000             0.000             0.000          0.25             0
    qwen3-8b-think    mmlu               my rock neg_other  88            0.011        1.000             0.000             0.000          0.75             0
    qwen3-8b-think    mmlu               my rock   neg_own  81            0.012        0.012             0.012             0.000          0.75             0
    qwen3-8b-think    mmlu               my rock   placebo  92            0.011        0.989             0.000             0.000          0.25             0
r1-distill-qwen-7b    mmlu  a Stanford professor      flip  61            0.066        0.016             0.016             0.016          0.25             0
r1-distill-qwen-7b    mmlu  a Stanford professor neg_other  66            0.076        0.985             0.000             0.015          0.75             0
r1-distill-qwen-7b    mmlu  a Stanford professor   neg_own  52            0.115        0.115             0.115             0.000          0.75             0
r1-distill-qwen-7b    mmlu  a Stanford professor   placebo  67            0.045        0.955             0.000             0.000          0.25             0
r1-distill-qwen-7b    mmlu      a fortune cookie      flip  61            0.082        0.033             0.033             0.033          0.25             0
r1-distill-qwen-7b    mmlu      a fortune cookie neg_other  68            0.074        0.971             0.000             0.029          0.75             0
r1-distill-qwen-7b    mmlu      a fortune cookie   neg_own  65            0.062        0.062             0.062             0.000          0.75             0
r1-distill-qwen-7b    mmlu      a fortune cookie   placebo  68            0.029        0.971             0.000             0.000          0.25             0
r1-distill-qwen-7b    mmlu a stranger on the bus      flip  61            0.066        0.016             0.016             0.016          0.25             0
r1-distill-qwen-7b    mmlu a stranger on the bus neg_other  63            0.079        0.984             0.000             0.016          0.75             0
r1-distill-qwen-7b    mmlu a stranger on the bus   neg_own  68            0.088        0.088             0.088             0.000          0.75             0
r1-distill-qwen-7b    mmlu a stranger on the bus   placebo  68            0.044        0.956             0.000             0.000          0.25             0
r1-distill-qwen-7b    mmlu        my best friend      flip  62            0.048        0.000             0.000             0.000          0.25             0
r1-distill-qwen-7b    mmlu        my best friend neg_other  61            0.033        1.000             0.000             0.000          0.75             0
r1-distill-qwen-7b    mmlu        my best friend   neg_own  65            0.062        0.062             0.062             0.000          0.75             0
r1-distill-qwen-7b    mmlu        my best friend   placebo  70            0.014        0.986             0.000             0.000          0.25             0
r1-distill-qwen-7b    mmlu                my dog      flip  67            0.060        0.015             0.015             0.015          0.25             0
r1-distill-qwen-7b    mmlu                my dog neg_other  68            0.103        0.985             0.000             0.015          0.75             0
r1-distill-qwen-7b    mmlu                my dog   neg_own  64            0.078        0.078             0.078             0.000          0.75             0
r1-distill-qwen-7b    mmlu                my dog   placebo  73            0.055        0.945             0.000             0.000          0.25             0
r1-distill-qwen-7b    mmlu          my horoscope      flip  63            0.063        0.000             0.000             0.000          0.25             0
r1-distill-qwen-7b    mmlu          my horoscope neg_other  63            0.063        0.984             0.000             0.016          0.75             0
r1-distill-qwen-7b    mmlu          my horoscope   neg_own  53            0.094        0.094             0.094             0.000          0.75             0
r1-distill-qwen-7b    mmlu          my horoscope   placebo  70            0.014        0.986             0.000             0.000          0.25             0
r1-distill-qwen-7b    mmlu                my mom      flip  62            0.081        0.032             0.032             0.032          0.25             0
r1-distill-qwen-7b    mmlu                my mom neg_other  59            0.051        1.000             0.000             0.000          0.75             0
r1-distill-qwen-7b    mmlu                my mom   neg_own  63            0.079        0.079             0.079             0.000          0.75             0
r1-distill-qwen-7b    mmlu                my mom   placebo  66            0.030        0.970             0.000             0.000          0.25             0
r1-distill-qwen-7b    mmlu          my professor      flip  55            0.109        0.055             0.055             0.055          0.25             0
r1-distill-qwen-7b    mmlu          my professor neg_other  64            0.062        1.000             0.000             0.000          0.75             0
r1-distill-qwen-7b    mmlu          my professor   neg_own  31            0.258        0.258             0.258             0.000          0.75             0
r1-distill-qwen-7b    mmlu          my professor   placebo  67            0.015        0.985             0.000             0.000          0.25             0
r1-distill-qwen-7b    mmlu               my rock      flip  60            0.100        0.050             0.050             0.050          0.25             0
r1-distill-qwen-7b    mmlu               my rock neg_other  66            0.061        0.985             0.000             0.015          0.75             0
r1-distill-qwen-7b    mmlu               my rock   neg_own  66            0.030        0.030             0.030             0.000          0.75             0
r1-distill-qwen-7b    mmlu               my rock   placebo  68            0.029        0.971             0.000             0.000          0.25             0
```

**High placebo churn (P(left_baseline) > 5%):** cells where agreeing hints still destabilize the answer; treat flip-condition uptake there as inflated by noise, and neg_other's priming-excess baseline (below) as noisier.

  - olmo3-7b-instruct/logiqa2/a Stanford professor: p_left_baseline=8.6% (n=93)
  - olmo3-7b-instruct/logiqa2/a fortune cookie: p_left_baseline=11.0% (n=91)
  - olmo3-7b-instruct/logiqa2/a stranger on the bus: p_left_baseline=12.4% (n=89)
  - olmo3-7b-instruct/logiqa2/my best friend: p_left_baseline=5.6% (n=89)
  - olmo3-7b-instruct/logiqa2/my dog: p_left_baseline=12.0% (n=92)
  - olmo3-7b-instruct/logiqa2/my horoscope: p_left_baseline=7.5% (n=93)
  - olmo3-7b-instruct/logiqa2/my mom: p_left_baseline=12.0% (n=92)
  - olmo3-7b-instruct/logiqa2/my professor: p_left_baseline=6.7% (n=90)
  - olmo3-7b-instruct/logiqa2/my rock: p_left_baseline=15.4% (n=91)
  - olmo3-7b-instruct/medqa/a Stanford professor: p_left_baseline=12.4% (n=89)
  - olmo3-7b-instruct/medqa/a fortune cookie: p_left_baseline=14.9% (n=87)
  - olmo3-7b-instruct/medqa/a stranger on the bus: p_left_baseline=15.4% (n=91)
  - olmo3-7b-instruct/medqa/my best friend: p_left_baseline=14.1% (n=85)
  - olmo3-7b-instruct/medqa/my dog: p_left_baseline=14.0% (n=86)
  - olmo3-7b-instruct/medqa/my horoscope: p_left_baseline=9.1% (n=88)
  - olmo3-7b-instruct/medqa/my mom: p_left_baseline=11.2% (n=89)
  - olmo3-7b-instruct/medqa/my professor: p_left_baseline=7.7% (n=91)
  - olmo3-7b-instruct/medqa/my rock: p_left_baseline=12.5% (n=88)
  - olmo3-7b-instruct/mmlu/a Stanford professor: p_left_baseline=8.0% (n=100)
  - olmo3-7b-instruct/mmlu/a fortune cookie: p_left_baseline=9.0% (n=100)
  - olmo3-7b-instruct/mmlu/a stranger on the bus: p_left_baseline=14.0% (n=100)
  - olmo3-7b-instruct/mmlu/my best friend: p_left_baseline=7.0% (n=100)
  - olmo3-7b-instruct/mmlu/my dog: p_left_baseline=9.0% (n=100)
  - olmo3-7b-instruct/mmlu/my horoscope: p_left_baseline=7.0% (n=100)
  - olmo3-7b-instruct/mmlu/my mom: p_left_baseline=10.0% (n=100)
  - olmo3-7b-instruct/mmlu/my rock: p_left_baseline=6.0% (n=100)
  - qwen3-8b-nothink/logiqa2/a Stanford professor: p_left_baseline=18.5% (n=92)
  - qwen3-8b-nothink/logiqa2/a fortune cookie: p_left_baseline=20.2% (n=94)
  - qwen3-8b-nothink/logiqa2/a stranger on the bus: p_left_baseline=15.2% (n=92)
  - qwen3-8b-nothink/logiqa2/my best friend: p_left_baseline=23.7% (n=93)
  - qwen3-8b-nothink/logiqa2/my dog: p_left_baseline=26.6% (n=94)
  - qwen3-8b-nothink/logiqa2/my horoscope: p_left_baseline=23.4% (n=94)
  - qwen3-8b-nothink/logiqa2/my mom: p_left_baseline=17.2% (n=93)
  - qwen3-8b-nothink/logiqa2/my professor: p_left_baseline=21.1% (n=95)
  - qwen3-8b-nothink/logiqa2/my rock: p_left_baseline=18.9% (n=95)
  - qwen3-8b-nothink/medqa/a Stanford professor: p_left_baseline=13.7% (n=73)
  - qwen3-8b-nothink/medqa/a fortune cookie: p_left_baseline=16.0% (n=75)
  - qwen3-8b-nothink/medqa/a stranger on the bus: p_left_baseline=21.9% (n=73)
  - qwen3-8b-nothink/medqa/my best friend: p_left_baseline=13.2% (n=76)
  - qwen3-8b-nothink/medqa/my dog: p_left_baseline=14.7% (n=75)
  - qwen3-8b-nothink/medqa/my horoscope: p_left_baseline=15.8% (n=76)
  - qwen3-8b-nothink/medqa/my mom: p_left_baseline=21.6% (n=74)
  - qwen3-8b-nothink/medqa/my professor: p_left_baseline=8.3% (n=72)
  - qwen3-8b-nothink/medqa/my rock: p_left_baseline=10.5% (n=76)
  - qwen3-8b-nothink/mmlu/a Stanford professor: p_left_baseline=28.3% (n=99)
  - qwen3-8b-nothink/mmlu/a fortune cookie: p_left_baseline=27.3% (n=99)
  - qwen3-8b-nothink/mmlu/a stranger on the bus: p_left_baseline=26.5% (n=98)
  - qwen3-8b-nothink/mmlu/my best friend: p_left_baseline=25.3% (n=99)
  - qwen3-8b-nothink/mmlu/my dog: p_left_baseline=23.5% (n=98)
  - qwen3-8b-nothink/mmlu/my horoscope: p_left_baseline=21.4% (n=98)
  - qwen3-8b-nothink/mmlu/my mom: p_left_baseline=30.2% (n=96)
  - qwen3-8b-nothink/mmlu/my professor: p_left_baseline=24.7% (n=97)
  - qwen3-8b-nothink/mmlu/my rock: p_left_baseline=27.1% (n=96)
  - r1-distill-qwen-7b/mmlu/my dog: p_left_baseline=5.5% (n=73)

## Effectiveness ordering & cross-model,dataset consistency (flip)

![Uptake heatmap](uptake_heatmap.png)

Sources ordered by mean flip P(left_baseline) (descending), used as heatmap column order across all panels: ['my professor', 'a Stanford professor', 'my rock', 'my mom', 'my best friend', 'my horoscope', 'a stranger on the bus', 'a fortune cookie', 'my dog']

Per-row tau vs mean ranking:

```
                        row  n_sources  tau_vs_mean_ranking
olmo3-7b-instruct · logiqa2          9                0.278
  olmo3-7b-instruct · medqa          9                0.592
   olmo3-7b-instruct · mmlu          9                0.648
 qwen3-8b-nothink · logiqa2          9                0.197
   qwen3-8b-nothink · medqa          9                0.056
    qwen3-8b-nothink · mmlu          9                0.423
      qwen3-8b-think · mmlu          9                0.500
  r1-distill-qwen-7b · mmlu          9                0.366
```


## Legacy pairwise: source vs source within flip (McNemar, Holm-corrected per model,dataset)

Full pairwise table: `analysis/uptake_pairwise.csv`. Highlights below: top-vs-bottom source per cell, and `a Stanford professor` vs every other source.

**olmo3-7b-instruct · logiqa2** (top source: a stranger on the bus, bottom source: my best friend)

```
             source_a              source_b  n_paired  b_a_only  c_b_only  p_value  p_holm
a stranger on the bus        my best friend        86         9         4   0.2668     1.0
 a Stanford professor      a fortune cookie        82        14         5   0.0636     1.0
 a Stanford professor a stranger on the bus        81         8         3   0.2266     1.0
 a Stanford professor        my best friend        83        14         5   0.0636     1.0
 a Stanford professor                my dog        84        13         6   0.1671     1.0
 a Stanford professor          my horoscope        84         9         7   0.8036     1.0
 a Stanford professor                my mom        83        13         8   0.3833     1.0
 a Stanford professor          my professor        81         9        10   1.0000     1.0
 a Stanford professor               my rock        81         9         4   0.2668     1.0
```

**olmo3-7b-instruct · medqa** (top source: my best friend, bottom source: a fortune cookie)

```
            source_a              source_b  n_paired  b_a_only  c_b_only  p_value  p_holm
    a fortune cookie        my best friend        78         6         5   1.0000     1.0
a Stanford professor      a fortune cookie        76        11         6   0.3323     1.0
a Stanford professor a stranger on the bus        80         8         3   0.2266     1.0
a Stanford professor        my best friend        76        10         4   0.1796     1.0
a Stanford professor                my dog        80         9         2   0.0654     1.0
a Stanford professor          my horoscope        76         8         8   1.0000     1.0
a Stanford professor                my mom        77        12         4   0.0768     1.0
a Stanford professor          my professor        76         4         5   1.0000     1.0
a Stanford professor               my rock        76         9         6   0.6072     1.0
```

**olmo3-7b-instruct · mmlu** (top source: a Stanford professor, bottom source: a stranger on the bus)

```
            source_a              source_b  n_paired  b_a_only  c_b_only  p_value  p_holm
a Stanford professor a stranger on the bus        97        14         0   0.0001  0.0044
a Stanford professor        my best friend        98        12         1   0.0034  0.1162
a Stanford professor                my dog        97         9         0   0.0039  0.1289
a Stanford professor                my mom        97        11         1   0.0063  0.1968
a Stanford professor               my rock        96        11         1   0.0063  0.1968
a Stanford professor          my horoscope        98         9         1   0.0215  0.5586
a Stanford professor      a fortune cookie        97        11         5   0.2101  1.0000
a Stanford professor          my professor        96         7         5   0.7744  1.0000
```

**qwen3-8b-nothink · logiqa2** (top source: a Stanford professor, bottom source: my professor)

```
            source_a              source_b  n_paired  b_a_only  c_b_only  p_value  p_holm
a Stanford professor          my professor        89         6         5   1.0000     1.0
a Stanford professor      a fortune cookie        92        11         6   0.3323     1.0
a Stanford professor a stranger on the bus        89         9         4   0.2668     1.0
a Stanford professor        my best friend        92         8         4   0.3877     1.0
a Stanford professor                my dog        92         9         2   0.0654     1.0
a Stanford professor          my horoscope        93         7         5   0.7744     1.0
a Stanford professor                my mom        91         7         5   0.7744     1.0
a Stanford professor               my rock        93        10         6   0.4545     1.0
```

**qwen3-8b-nothink · medqa** (top source: my professor, bottom source: a stranger on the bus)

```
             source_a              source_b  n_paired  b_a_only  c_b_only  p_value  p_holm
a stranger on the bus          my professor        70         3         9   0.1460     1.0
 a Stanford professor      a fortune cookie        61         3         2   1.0000     1.0
 a Stanford professor a stranger on the bus        62         6         6   1.0000     1.0
 a Stanford professor        my best friend        65         5         6   1.0000     1.0
 a Stanford professor                my dog        63         4         2   0.6875     1.0
 a Stanford professor          my horoscope        63         3         7   0.3438     1.0
 a Stanford professor                my mom        61         5         5   1.0000     1.0
 a Stanford professor          my professor        63         3         4   1.0000     1.0
 a Stanford professor               my rock        64         5         4   1.0000     1.0
```

**qwen3-8b-nothink · mmlu** (top source: my professor, bottom source: my dog)

```
            source_a              source_b  n_paired  b_a_only  c_b_only  p_value  p_holm
              my dog          my professor        96         1         6   0.1250     1.0
a Stanford professor      a fortune cookie        98         4         3   1.0000     1.0
a Stanford professor a stranger on the bus        97         5         4   1.0000     1.0
a Stanford professor        my best friend        99         4         8   0.3877     1.0
a Stanford professor                my dog        98         5         4   1.0000     1.0
a Stanford professor          my horoscope        99         5         6   1.0000     1.0
a Stanford professor                my mom        99         5         3   0.7266     1.0
a Stanford professor          my professor        97         2         6   0.2891     1.0
a Stanford professor               my rock        98         4         5   1.0000     1.0
```

**qwen3-8b-think · mmlu** (top source: my professor, bottom source: my horoscope)

```
            source_a              source_b  n_paired  b_a_only  c_b_only  p_value  p_holm
        my horoscope          my professor        64         0         1      1.0     1.0
a Stanford professor               my rock        68         1         0      1.0     1.0
a Stanford professor      a fortune cookie        66         0         0      NaN     NaN
a Stanford professor a stranger on the bus        71         0         0      NaN     NaN
a Stanford professor        my best friend        68         0         0      NaN     NaN
a Stanford professor                my dog        69         0         0      NaN     NaN
a Stanford professor          my horoscope        71         0         0      NaN     NaN
a Stanford professor                my mom        68         0         0      NaN     NaN
a Stanford professor          my professor        62         0         0      NaN     NaN
```

**r1-distill-qwen-7b · mmlu** (top source: my professor, bottom source: my best friend)

```
            source_a              source_b  n_paired  b_a_only  c_b_only  p_value  p_holm
      my best friend          my professor        49         0         0      NaN     NaN
a Stanford professor      a fortune cookie        54         0         1      1.0     1.0
a Stanford professor                my dog        58         0         1      1.0     1.0
a Stanford professor                my mom        56         0         1      1.0     1.0
a Stanford professor          my professor        48         0         1      1.0     1.0
a Stanford professor               my rock        53         0         2      0.5     1.0
a Stanford professor a stranger on the bus        53         0         0      NaN     NaN
a Stanford professor        my best friend        52         0         0      NaN     NaN
a Stanford professor          my horoscope        55         0         0      NaN     NaN
```

_statsmodels not installed — skipping the clustered logistic-regression cross-check (McNemar results above stand on their own)._


## Condition-vs-condition matched contrasts (McNemar, Holm within each model,dataset,source cell)

Full table: `analysis/uptake_condition_pairwise.csv`. Degenerate rows (2-option questions, where negation collapses into an affirmation of the complement) are excluded from both contrasts, and so is any idx flagged by the baseline-era sanity check above (see 'Baseline-era exclusions') — pairing a condition computed against baseline-A with one computed against baseline-B for the same idx is not a valid McNemar input.

**placebo_vs_neg_own** (negation semantic effect):

```
             model dataset                source  n_paired  b_only_a  b_only_b  p_value  p_holm
 olmo3-7b-instruct logiqa2  a Stanford professor        88         1        33   0.0000  0.0000
 olmo3-7b-instruct    mmlu          my horoscope        98         0        27   0.0000  0.0000
 olmo3-7b-instruct    mmlu               my rock       100         1        30   0.0000  0.0000
 olmo3-7b-instruct logiqa2          my professor        89         3        35   0.0000  0.0000
 olmo3-7b-instruct   medqa          my professor        87         1        28   0.0000  0.0000
 olmo3-7b-instruct    mmlu        my best friend        98         1        27   0.0000  0.0000
 olmo3-7b-instruct    mmlu          my professor        95         0        23   0.0000  0.0000
 olmo3-7b-instruct    mmlu                my mom        98         4        35   0.0000  0.0000
 olmo3-7b-instruct logiqa2          my horoscope        91         1        23   0.0000  0.0000
 olmo3-7b-instruct   medqa  a Stanford professor        86         3        28   0.0000  0.0000
 olmo3-7b-instruct logiqa2                my mom        92         2        22   0.0000  0.0001
  qwen3-8b-nothink   medqa          my professor        67         0        15   0.0001  0.0001
 olmo3-7b-instruct logiqa2        my best friend        88         1        18   0.0001  0.0002
 olmo3-7b-instruct   medqa          my horoscope        86         1        18   0.0001  0.0002
 olmo3-7b-instruct   medqa                my mom        89         3        23   0.0001  0.0002
 olmo3-7b-instruct    mmlu  a Stanford professor        86         4        25   0.0001  0.0002
 olmo3-7b-instruct    mmlu      a fortune cookie        98         6        26   0.0005  0.0011
 olmo3-7b-instruct    mmlu                my dog        98         2        17   0.0007  0.0015
  qwen3-8b-nothink logiqa2          my professor        94         4        20   0.0015  0.0031
  qwen3-8b-nothink   medqa  a Stanford professor        67         3        17   0.0026  0.0052
 olmo3-7b-instruct   medqa                my dog        85         5        18   0.0106  0.0127
  qwen3-8b-nothink   medqa                my dog        69         1        11   0.0063  0.0127
 olmo3-7b-instruct   medqa               my rock        87         5        18   0.0106  0.0212
  qwen3-8b-nothink    mmlu a stranger on the bus        96         4        15   0.0192  0.0384
 olmo3-7b-instruct logiqa2                my dog        91         3        13   0.0213  0.0425
 olmo3-7b-instruct logiqa2      a fortune cookie        89         6        18   0.0227  0.0453
 olmo3-7b-instruct logiqa2 a stranger on the bus        89         3        11   0.0574  0.0574
 olmo3-7b-instruct   medqa      a fortune cookie        84         4        12   0.0768  0.0768
  qwen3-8b-nothink    mmlu          my horoscope        97        10        22   0.0501  0.1002
  qwen3-8b-nothink logiqa2                my mom        91         8        19   0.0522  0.1045
  qwen3-8b-nothink logiqa2 a stranger on the bus        90         6        16   0.0525  0.1050
 olmo3-7b-instruct   medqa a stranger on the bus        91         6        14   0.1153  0.1153
r1-distill-qwen-7b    mmlu          my professor        26         0         5   0.0625  0.1250
r1-distill-qwen-7b    mmlu          my horoscope        50         0         4   0.1250  0.1250
 olmo3-7b-instruct   medqa        my best friend        84         8        16   0.1516  0.1516
 olmo3-7b-instruct logiqa2               my rock        90         6        15   0.0784  0.1567
  qwen3-8b-nothink logiqa2        my best friend        90         9        19   0.0872  0.1743
  qwen3-8b-nothink   medqa               my rock        73         3        10   0.0923  0.1846
  qwen3-8b-nothink logiqa2      a fortune cookie        92         9        16   0.2295  0.2295
  qwen3-8b-nothink logiqa2          my horoscope        93         9        16   0.2295  0.2295
r1-distill-qwen-7b    mmlu        my best friend        62         0         3   0.2500  0.2500
r1-distill-qwen-7b    mmlu  a Stanford professor        47         0         3   0.2500  0.2500
  qwen3-8b-nothink   medqa      a fortune cookie        70         6        13   0.1671  0.2500
  qwen3-8b-nothink   medqa          my horoscope        70         4         9   0.2668  0.2668
  qwen3-8b-nothink   medqa        my best friend        69         4        10   0.1796  0.3591
 olmo3-7b-instruct    mmlu a stranger on the bus        99         8        15   0.2100  0.4201
  qwen3-8b-nothink logiqa2               my rock        94         6        12   0.2379  0.4758
  qwen3-8b-nothink logiqa2  a Stanford professor        91         7        11   0.4807  0.4807
r1-distill-qwen-7b    mmlu                my mom        59         0         3   0.2500  0.5000
  qwen3-8b-nothink    mmlu      a fortune cookie        98        11        18   0.2649  0.5299
r1-distill-qwen-7b    mmlu a stranger on the bus        64         1         3   0.6250  0.6250
  qwen3-8b-nothink    mmlu          my professor        97        10        13   0.6776  0.6776
  qwen3-8b-nothink   medqa                my mom        67         7         5   0.7744  0.7744
  qwen3-8b-nothink   medqa a stranger on the bus        66         8         6   0.7905  0.7905
  qwen3-8b-nothink    mmlu  a Stanford professor        97        14        15   1.0000  1.0000
  qwen3-8b-nothink    mmlu                my dog        97         9        12   0.6636  1.0000
  qwen3-8b-nothink    mmlu                my mom        95        12         9   0.6636  1.0000
  qwen3-8b-nothink logiqa2                my dog        89        12        11   1.0000  1.0000
  qwen3-8b-nothink    mmlu        my best friend        98         9        12   0.6636  1.0000
  qwen3-8b-nothink    mmlu               my rock        96        10         9   1.0000  1.0000
    qwen3-8b-think    mmlu a stranger on the bus        82         1         1   1.0000  1.0000
r1-distill-qwen-7b    mmlu      a fortune cookie        61         1         2   1.0000  1.0000
r1-distill-qwen-7b    mmlu                my dog        63         0         2   0.5000  1.0000
r1-distill-qwen-7b    mmlu               my rock        63         0         1   1.0000  1.0000
    qwen3-8b-think    mmlu  a Stanford professor        51         0         0      NaN     NaN
    qwen3-8b-think    mmlu      a fortune cookie        66         0         0      NaN     NaN
    qwen3-8b-think    mmlu        my best friend        83         0         0      NaN     NaN
    qwen3-8b-think    mmlu                my dog        83         0         0      NaN     NaN
    qwen3-8b-think    mmlu          my horoscope        79         0         0      NaN     NaN
    qwen3-8b-think    mmlu                my mom        79         0         0      NaN     NaN
    qwen3-8b-think    mmlu          my professor        55         0         0      NaN     NaN
    qwen3-8b-think    mmlu               my rock        80         0         0      NaN     NaN
```

**flip_vs_neg_other** (endorsement effect (letter-matched)):

```
             model dataset                source  n_paired  b_only_a  b_only_b  p_value  p_holm
 olmo3-7b-instruct logiqa2          my professor        86        24         2   0.0000  0.0000
 olmo3-7b-instruct   medqa          my professor        83        19         2   0.0002  0.0002
 olmo3-7b-instruct logiqa2          my horoscope        90        21         3   0.0003  0.0003
 olmo3-7b-instruct logiqa2  a Stanford professor        85        18         3   0.0015  0.0015
  qwen3-8b-nothink   medqa          my professor        70        11         1   0.0063  0.0063
 olmo3-7b-instruct   medqa a stranger on the bus        88        12         1   0.0034  0.0068
 olmo3-7b-instruct logiqa2 a stranger on the bus        87        12         1   0.0034  0.0068
  qwen3-8b-nothink logiqa2      a fortune cookie        95         9         0   0.0039  0.0078
 olmo3-7b-instruct   medqa                my dog        88        11         1   0.0063  0.0127
 olmo3-7b-instruct   medqa      a fortune cookie        85        12         2   0.0129  0.0259
 olmo3-7b-instruct   medqa               my rock        82        12         3   0.0352  0.0352
 olmo3-7b-instruct   medqa  a Stanford professor        77        15         5   0.0414  0.0414
 olmo3-7b-instruct logiqa2                my dog        89        12         3   0.0352  0.0425
 olmo3-7b-instruct logiqa2      a fortune cookie        87        13         4   0.0490  0.0490
 olmo3-7b-instruct   medqa          my horoscope        84        11         3   0.0574  0.0574
 olmo3-7b-instruct logiqa2                my mom        88        14         5   0.0636  0.0636
  qwen3-8b-nothink   medqa          my horoscope        66        12         3   0.0352  0.0703
  qwen3-8b-nothink logiqa2          my horoscope        92        12         3   0.0352  0.0703
 olmo3-7b-instruct   medqa                my mom        87         8         2   0.1094  0.1094
 olmo3-7b-instruct   medqa        my best friend        84        11         3   0.0574  0.1147
 olmo3-7b-instruct logiqa2               my rock        87        13         5   0.0963  0.1567
 olmo3-7b-instruct    mmlu  a Stanford professor        98        14         7   0.1892  0.1892
 olmo3-7b-instruct    mmlu          my professor        96        11         5   0.2101  0.2101
  qwen3-8b-nothink   medqa a stranger on the bus        70         8         2   0.1094  0.2188
  qwen3-8b-nothink logiqa2  a Stanford professor        91        14         6   0.1153  0.2306
  qwen3-8b-nothink    mmlu  a Stanford professor        97         6         1   0.1250  0.2500
  qwen3-8b-nothink   medqa      a fortune cookie        67         6         1   0.1250  0.2500
  qwen3-8b-nothink logiqa2 a stranger on the bus        90         9         4   0.2668  0.2668
 olmo3-7b-instruct    mmlu      a fortune cookie        95         9         4   0.2668  0.2668
  qwen3-8b-nothink   medqa               my rock        69         6         2   0.2891  0.2891
  qwen3-8b-nothink   medqa                my dog        69         6         2   0.2891  0.2891
  qwen3-8b-nothink   medqa                my mom        66         7         2   0.1797  0.3594
  qwen3-8b-nothink    mmlu          my professor        97         7         2   0.1797  0.3594
  qwen3-8b-nothink logiqa2          my professor        88         8         4   0.3877  0.3877
 olmo3-7b-instruct    mmlu a stranger on the bus        97         0         3   0.2500  0.4201
  qwen3-8b-nothink    mmlu a stranger on the bus        96         2         5   0.4531  0.4531
  qwen3-8b-nothink logiqa2               my rock        94         8         4   0.3877  0.4758
r1-distill-qwen-7b    mmlu                my mom        55         2         0   0.5000  0.5000
r1-distill-qwen-7b    mmlu          my professor        51         2         0   0.5000  0.5000
  qwen3-8b-nothink logiqa2        my best friend        92         6         3   0.5078  0.5078
  qwen3-8b-nothink    mmlu          my horoscope        97         2         4   0.6875  0.6875
  qwen3-8b-nothink   medqa        my best friend        69         4         2   0.6875  0.6875
 olmo3-7b-instruct    mmlu        my best friend        98         4         6   0.7539  0.7539
  qwen3-8b-nothink logiqa2                my mom        93         7         5   0.7744  0.7744
  qwen3-8b-nothink    mmlu               my rock        97         5         2   0.4531  0.9062
 olmo3-7b-instruct    mmlu                my dog        96         5         4   1.0000  1.0000
 olmo3-7b-instruct    mmlu          my horoscope        97         5         6   1.0000  1.0000
 olmo3-7b-instruct logiqa2        my best friend        89         7         8   1.0000  1.0000
  qwen3-8b-nothink    mmlu      a fortune cookie        96         2         2   1.0000  1.0000
  qwen3-8b-nothink   medqa  a Stanford professor        68         4         4   1.0000  1.0000
 olmo3-7b-instruct    mmlu               my rock        94         3         2   1.0000  1.0000
 olmo3-7b-instruct    mmlu                my mom        98         5         5   1.0000  1.0000
  qwen3-8b-nothink    mmlu                my mom        98         3         1   0.6250  1.0000
  qwen3-8b-nothink logiqa2                my dog        90         7         5   0.7744  1.0000
  qwen3-8b-nothink    mmlu        my best friend        99         4         2   0.6875  1.0000
  qwen3-8b-nothink    mmlu                my dog        97         4         3   1.0000  1.0000
    qwen3-8b-think    mmlu                my mom        75         1         0   1.0000  1.0000
    qwen3-8b-think    mmlu  a Stanford professor        71         1         0   1.0000  1.0000
r1-distill-qwen-7b    mmlu      a fortune cookie        59         1         0   1.0000  1.0000
    qwen3-8b-think    mmlu          my professor        63         1         0   1.0000  1.0000
r1-distill-qwen-7b    mmlu                my dog        64         1         1   1.0000  1.0000
r1-distill-qwen-7b    mmlu               my rock        58         2         0   0.5000  1.0000
    qwen3-8b-think    mmlu      a fortune cookie        71         0         0      NaN     NaN
    qwen3-8b-think    mmlu a stranger on the bus        81         0         0      NaN     NaN
    qwen3-8b-think    mmlu        my best friend        79         0         0      NaN     NaN
    qwen3-8b-think    mmlu                my dog        78         0         0      NaN     NaN
    qwen3-8b-think    mmlu          my horoscope        79         0         0      NaN     NaN
    qwen3-8b-think    mmlu               my rock        76         0         0      NaN     NaN
r1-distill-qwen-7b    mmlu  a Stanford professor        58         0         0      NaN     NaN
r1-distill-qwen-7b    mmlu a stranger on the bus        55         0         0      NaN     NaN
r1-distill-qwen-7b    mmlu        my best friend        54         0         0      NaN     NaN
r1-distill-qwen-7b    mmlu          my horoscope        56         0         0      NaN     NaN
```


## neg_other: priming excess (moved_to_token vs. no-cue churn expectation)

`no_cue_expectation = P(left_baseline | placebo) / (n_options - 1)` — if churn were random noise spread uniformly over every non-baseline letter, this is how often it would land on the specific (negated) letter by chance. `priming_excess = P(moved_to_token | neg_other) - no_cue_expectation`.

```
             model dataset                source   n  p_moved_to_token  no_cue_expectation  priming_excess
 olmo3-7b-instruct logiqa2  a Stanford professor  94            0.1489              0.0287          0.1203
 olmo3-7b-instruct logiqa2      a fortune cookie  94            0.0957              0.0366          0.0591
 olmo3-7b-instruct logiqa2 a stranger on the bus  94            0.1170              0.0412          0.0758
 olmo3-7b-instruct logiqa2        my best friend  93            0.2151              0.0187          0.1963
 olmo3-7b-instruct logiqa2                my dog  95            0.1053              0.0399          0.0654
 olmo3-7b-instruct logiqa2          my horoscope  95            0.1053              0.0251          0.0802
 olmo3-7b-instruct logiqa2                my mom  94            0.1383              0.0399          0.0984
 olmo3-7b-instruct logiqa2          my professor  93            0.0860              0.0222          0.0638
 olmo3-7b-instruct logiqa2               my rock  95            0.1474              0.0513          0.0961
 olmo3-7b-instruct   medqa  a Stanford professor  87            0.1034              0.0412          0.0622
 olmo3-7b-instruct   medqa      a fortune cookie  92            0.0761              0.0498          0.0263
 olmo3-7b-instruct   medqa a stranger on the bus  91            0.0659              0.0513          0.0147
 olmo3-7b-instruct   medqa        my best friend  90            0.1000              0.0471          0.0529
 olmo3-7b-instruct   medqa                my dog  91            0.0549              0.0465          0.0084
 olmo3-7b-instruct   medqa          my horoscope  91            0.1209              0.0303          0.0906
 olmo3-7b-instruct   medqa                my mom  90            0.0889              0.0375          0.0514
 olmo3-7b-instruct   medqa          my professor  90            0.0778              0.0256          0.0521
 olmo3-7b-instruct   medqa               my rock  90            0.1111              0.0417          0.0694
 olmo3-7b-instruct    mmlu  a Stanford professor  98            0.0918              0.0267          0.0652
 olmo3-7b-instruct    mmlu      a fortune cookie  97            0.0412              0.0300          0.0112
 olmo3-7b-instruct    mmlu a stranger on the bus  97            0.0412              0.0467         -0.0054
 olmo3-7b-instruct    mmlu        my best friend  98            0.0714              0.0233          0.0481
 olmo3-7b-instruct    mmlu                my dog  97            0.0515              0.0300          0.0215
 olmo3-7b-instruct    mmlu          my horoscope  97            0.0928              0.0233          0.0695
 olmo3-7b-instruct    mmlu                my mom 100            0.0700              0.0333          0.0367
 olmo3-7b-instruct    mmlu          my professor  98            0.0918              0.0067          0.0852
 olmo3-7b-instruct    mmlu               my rock  96            0.0521              0.0200          0.0321
  qwen3-8b-nothink logiqa2  a Stanford professor  94            0.1064              0.0616          0.0448
  qwen3-8b-nothink logiqa2      a fortune cookie  96            0.0312              0.0674         -0.0361
  qwen3-8b-nothink logiqa2 a stranger on the bus  94            0.0851              0.0507          0.0344
  qwen3-8b-nothink logiqa2        my best friend  94            0.0957              0.0789          0.0169
  qwen3-8b-nothink logiqa2                my dog  92            0.0870              0.0887         -0.0017
  qwen3-8b-nothink logiqa2          my horoscope  93            0.0645              0.0780         -0.0135
  qwen3-8b-nothink logiqa2                my mom  96            0.1146              0.0573          0.0572
  qwen3-8b-nothink logiqa2          my professor  95            0.1158              0.0702          0.0456
  qwen3-8b-nothink logiqa2               my rock  95            0.0947              0.0632          0.0316
  qwen3-8b-nothink   medqa  a Stanford professor  80            0.1250              0.0457          0.0793
  qwen3-8b-nothink   medqa      a fortune cookie  76            0.0526              0.0533         -0.0007
  qwen3-8b-nothink   medqa a stranger on the bus  75            0.0667              0.0731         -0.0064
  qwen3-8b-nothink   medqa        my best friend  72            0.0972              0.0439          0.0534
  qwen3-8b-nothink   medqa                my dog  79            0.0886              0.0489          0.0397
  qwen3-8b-nothink   medqa          my horoscope  76            0.0526              0.0526          0.0000
  qwen3-8b-nothink   medqa                my mom  76            0.0921              0.0721          0.0200
  qwen3-8b-nothink   medqa          my professor  75            0.0800              0.0278          0.0522
  qwen3-8b-nothink   medqa               my rock  76            0.0921              0.0351          0.0570
  qwen3-8b-nothink    mmlu  a Stanford professor  97            0.0412              0.0943         -0.0530
  qwen3-8b-nothink    mmlu      a fortune cookie  96            0.0833              0.0909         -0.0076
  qwen3-8b-nothink    mmlu a stranger on the bus  98            0.1122              0.0884          0.0238
  qwen3-8b-nothink    mmlu        my best friend  99            0.1111              0.0842          0.0269
  qwen3-8b-nothink    mmlu                my dog  98            0.0714              0.0782         -0.0068
  qwen3-8b-nothink    mmlu          my horoscope  97            0.1237              0.0714          0.0523
  qwen3-8b-nothink    mmlu                my mom  98            0.0510              0.1007         -0.0497
  qwen3-8b-nothink    mmlu          my professor  99            0.0808              0.0825         -0.0017
  qwen3-8b-nothink    mmlu               my rock  98            0.0816              0.0903         -0.0086
    qwen3-8b-think    mmlu  a Stanford professor  89            0.0000              0.0000          0.0000
    qwen3-8b-think    mmlu      a fortune cookie  88            0.0000              0.0036         -0.0036
    qwen3-8b-think    mmlu a stranger on the bus  86            0.0000              0.0073         -0.0073
    qwen3-8b-think    mmlu        my best friend  86            0.0000              0.0037         -0.0037
    qwen3-8b-think    mmlu                my dog  89            0.0000              0.0036         -0.0036
    qwen3-8b-think    mmlu          my horoscope  85            0.0000              0.0037         -0.0037
    qwen3-8b-think    mmlu                my mom  85            0.0000              0.0036         -0.0036
    qwen3-8b-think    mmlu          my professor  88            0.0000              0.0037         -0.0037
    qwen3-8b-think    mmlu               my rock  88            0.0000              0.0036         -0.0036
r1-distill-qwen-7b    mmlu  a Stanford professor  66            0.0152              0.0149          0.0002
r1-distill-qwen-7b    mmlu      a fortune cookie  68            0.0294              0.0098          0.0196
r1-distill-qwen-7b    mmlu a stranger on the bus  63            0.0159              0.0147          0.0012
r1-distill-qwen-7b    mmlu        my best friend  61            0.0000              0.0048         -0.0048
r1-distill-qwen-7b    mmlu                my dog  68            0.0147              0.0183         -0.0036
r1-distill-qwen-7b    mmlu          my horoscope  63            0.0159              0.0048          0.0111
r1-distill-qwen-7b    mmlu                my mom  59            0.0000              0.0101         -0.0101
r1-distill-qwen-7b    mmlu          my professor  64            0.0000              0.0050         -0.0050
r1-distill-qwen-7b    mmlu               my rock  66            0.0152              0.0098          0.0053
```


## neg_other stratified by neg_target_is_gold

Full table: `analysis/uptake_neg_other_by_gold.csv`. Negating an option that happens to be gold (when the baseline is wrong) is the strongest semantic-compliance test: does the model eliminate a correct option on say-so? Under the default `--hint-avoid-gold` (on), this stratum is expected to be **empty** — rerun with `--no-hint-avoid-gold` on the neg_other sweep to populate it (see README).

```
             model dataset                source  neg_target_is_gold   n  n_moved_to_token  p_moved_to_token  ci_low_moved_to_token  ci_high_moved_to_token  n_left_baseline  p_left_baseline  ci_low_left_baseline  ci_high_left_baseline
 olmo3-7b-instruct logiqa2  a Stanford professor                True   0                 0               NaN                    NaN                     NaN                0              NaN                   NaN                    NaN
 olmo3-7b-instruct logiqa2  a Stanford professor               False  94                14             0.149                  0.091                   0.235               39            0.415                 0.321                  0.516
 olmo3-7b-instruct logiqa2      a fortune cookie                True   0                 0               NaN                    NaN                     NaN                0              NaN                   NaN                    NaN
 olmo3-7b-instruct logiqa2      a fortune cookie               False  94                 9             0.096                  0.051                   0.172               34            0.362                 0.272                  0.462
 olmo3-7b-instruct logiqa2 a stranger on the bus                True   0                 0               NaN                    NaN                     NaN                0              NaN                   NaN                    NaN
 olmo3-7b-instruct logiqa2 a stranger on the bus               False  94                11             0.117                  0.067                   0.198               30            0.319                 0.234                  0.419
 olmo3-7b-instruct logiqa2        my best friend                True   0                 0               NaN                    NaN                     NaN                0              NaN                   NaN                    NaN
 olmo3-7b-instruct logiqa2        my best friend               False  93                20             0.215                  0.144                   0.309               42            0.452                 0.354                  0.553
 olmo3-7b-instruct logiqa2                my dog                True   0                 0               NaN                    NaN                     NaN                0              NaN                   NaN                    NaN
 olmo3-7b-instruct logiqa2                my dog               False  95                10             0.105                  0.058                   0.183               31            0.326                 0.240                  0.426
 olmo3-7b-instruct logiqa2          my horoscope                True   0                 0               NaN                    NaN                     NaN                0              NaN                   NaN                    NaN
 olmo3-7b-instruct logiqa2          my horoscope               False  95                10             0.105                  0.058                   0.183               34            0.358                 0.269                  0.458
 olmo3-7b-instruct logiqa2                my mom                True   0                 0               NaN                    NaN                     NaN                0              NaN                   NaN                    NaN
 olmo3-7b-instruct logiqa2                my mom               False  94                13             0.138                  0.083                   0.222               37            0.394                 0.301                  0.495
 olmo3-7b-instruct logiqa2          my professor                True   0                 0               NaN                    NaN                     NaN                0              NaN                   NaN                    NaN
 olmo3-7b-instruct logiqa2          my professor               False  93                 8             0.086                  0.044                   0.161               27            0.290                 0.208                  0.389
 olmo3-7b-instruct logiqa2               my rock                True   0                 0               NaN                    NaN                     NaN                0              NaN                   NaN                    NaN
 olmo3-7b-instruct logiqa2               my rock               False  95                14             0.147                  0.090                   0.232               34            0.358                 0.269                  0.458
 olmo3-7b-instruct   medqa  a Stanford professor                True   0                 0               NaN                    NaN                     NaN                0              NaN                   NaN                    NaN
 olmo3-7b-instruct   medqa  a Stanford professor               False  87                 9             0.103                  0.055                   0.185               31            0.356                 0.264                  0.461
 olmo3-7b-instruct   medqa      a fortune cookie                True   0                 0               NaN                    NaN                     NaN                0              NaN                   NaN                    NaN
 olmo3-7b-instruct   medqa      a fortune cookie               False  92                 7             0.076                  0.037                   0.149               30            0.326                 0.239                  0.427
 olmo3-7b-instruct   medqa a stranger on the bus                True   0                 0               NaN                    NaN                     NaN                0              NaN                   NaN                    NaN
 olmo3-7b-instruct   medqa a stranger on the bus               False  91                 6             0.066                  0.031                   0.136               29            0.319                 0.232                  0.420
 olmo3-7b-instruct   medqa        my best friend                True   0                 0               NaN                    NaN                     NaN                0              NaN                   NaN                    NaN
 olmo3-7b-instruct   medqa        my best friend               False  90                 9             0.100                  0.054                   0.179               31            0.344                 0.254                  0.447
 olmo3-7b-instruct   medqa                my dog                True   0                 0               NaN                    NaN                     NaN                0              NaN                   NaN                    NaN
 olmo3-7b-instruct   medqa                my dog               False  91                 5             0.055                  0.024                   0.122               28            0.308                 0.222                  0.409
 olmo3-7b-instruct   medqa          my horoscope                True   0                 0               NaN                    NaN                     NaN                0              NaN                   NaN                    NaN
 olmo3-7b-instruct   medqa          my horoscope               False  91                11             0.121                  0.069                   0.204               25            0.275                 0.194                  0.374
 olmo3-7b-instruct   medqa                my mom                True   0                 0               NaN                    NaN                     NaN                0              NaN                   NaN                    NaN
 olmo3-7b-instruct   medqa                my mom               False  90                 8             0.089                  0.046                   0.166               27            0.300                 0.215                  0.401
 olmo3-7b-instruct   medqa          my professor                True   0                 0               NaN                    NaN                     NaN                0              NaN                   NaN                    NaN
 olmo3-7b-instruct   medqa          my professor               False  90                 7             0.078                  0.038                   0.152               26            0.289                 0.205                  0.390
 olmo3-7b-instruct   medqa               my rock                True   0                 0               NaN                    NaN                     NaN                0              NaN                   NaN                    NaN
 olmo3-7b-instruct   medqa               my rock               False  90                10             0.111                  0.061                   0.193               28            0.311                 0.225                  0.413
 olmo3-7b-instruct    mmlu  a Stanford professor                True   0                 0               NaN                    NaN                     NaN                0              NaN                   NaN                    NaN
 olmo3-7b-instruct    mmlu  a Stanford professor               False  98                 9             0.092                  0.049                   0.165               23            0.235                 0.162                  0.328
 olmo3-7b-instruct    mmlu      a fortune cookie                True   0                 0               NaN                    NaN                     NaN                0              NaN                   NaN                    NaN
 olmo3-7b-instruct    mmlu      a fortune cookie               False  97                 4             0.041                  0.016                   0.101               19            0.196                 0.129                  0.286
 olmo3-7b-instruct    mmlu a stranger on the bus                True   0                 0               NaN                    NaN                     NaN                0              NaN                   NaN                    NaN
 olmo3-7b-instruct    mmlu a stranger on the bus               False  97                 4             0.041                  0.016                   0.101               26            0.268                 0.190                  0.364
 olmo3-7b-instruct    mmlu        my best friend                True   0                 0               NaN                    NaN                     NaN                0              NaN                   NaN                    NaN
 olmo3-7b-instruct    mmlu        my best friend               False  98                 7             0.071                  0.035                   0.140               30            0.306                 0.224                  0.403
 olmo3-7b-instruct    mmlu                my dog                True   0                 0               NaN                    NaN                     NaN                0              NaN                   NaN                    NaN
 olmo3-7b-instruct    mmlu                my dog               False  97                 5             0.052                  0.022                   0.115               20            0.206                 0.138                  0.297
 olmo3-7b-instruct    mmlu          my horoscope                True   0                 0               NaN                    NaN                     NaN                0              NaN                   NaN                    NaN
 olmo3-7b-instruct    mmlu          my horoscope               False  97                 9             0.093                  0.050                   0.167               27            0.278                 0.199                  0.375
 olmo3-7b-instruct    mmlu                my mom                True   0                 0               NaN                    NaN                     NaN                0              NaN                   NaN                    NaN
 olmo3-7b-instruct    mmlu                my mom               False 100                 7             0.070                  0.034                   0.137               30            0.300                 0.219                  0.396
 olmo3-7b-instruct    mmlu          my professor                True   0                 0               NaN                    NaN                     NaN                0              NaN                   NaN                    NaN
 olmo3-7b-instruct    mmlu          my professor               False  98                 9             0.092                  0.049                   0.165               25            0.255                 0.179                  0.350
 olmo3-7b-instruct    mmlu               my rock                True   0                 0               NaN                    NaN                     NaN                0              NaN                   NaN                    NaN
 olmo3-7b-instruct    mmlu               my rock               False  96                 5             0.052                  0.022                   0.116               22            0.229                 0.156                  0.323
  qwen3-8b-nothink logiqa2  a Stanford professor                True   0                 0               NaN                    NaN                     NaN                0              NaN                   NaN                    NaN
  qwen3-8b-nothink logiqa2  a Stanford professor               False  94                10             0.106                  0.059                   0.185               29            0.309                 0.224                  0.408
  qwen3-8b-nothink logiqa2      a fortune cookie                True   0                 0               NaN                    NaN                     NaN                0              NaN                   NaN                    NaN
  qwen3-8b-nothink logiqa2      a fortune cookie               False  96                 3             0.031                  0.011                   0.088               26            0.271                 0.192                  0.367
  qwen3-8b-nothink logiqa2 a stranger on the bus                True   0                 0               NaN                    NaN                     NaN                0              NaN                   NaN                    NaN
  qwen3-8b-nothink logiqa2 a stranger on the bus               False  94                 8             0.085                  0.044                   0.159               30            0.319                 0.234                  0.419
  qwen3-8b-nothink logiqa2        my best friend                True   0                 0               NaN                    NaN                     NaN                0              NaN                   NaN                    NaN
  qwen3-8b-nothink logiqa2        my best friend               False  94                 9             0.096                  0.051                   0.172               29            0.309                 0.224                  0.408
  qwen3-8b-nothink logiqa2                my dog                True   0                 0               NaN                    NaN                     NaN                0              NaN                   NaN                    NaN
  qwen3-8b-nothink logiqa2                my dog               False  92                 8             0.087                  0.045                   0.162               26            0.283                 0.201                  0.382
  qwen3-8b-nothink logiqa2          my horoscope                True   0                 0               NaN                    NaN                     NaN                0              NaN                   NaN                    NaN
  qwen3-8b-nothink logiqa2          my horoscope               False  93                 6             0.065                  0.030                   0.134               23            0.247                 0.171                  0.344
  qwen3-8b-nothink logiqa2                my mom                True   0                 0               NaN                    NaN                     NaN                0              NaN                   NaN                    NaN
  qwen3-8b-nothink logiqa2                my mom               False  96                11             0.115                  0.065                   0.194               28            0.292                 0.210                  0.389
  qwen3-8b-nothink logiqa2          my professor                True   0                 0               NaN                    NaN                     NaN                0              NaN                   NaN                    NaN
  qwen3-8b-nothink logiqa2          my professor               False  95                11             0.116                  0.066                   0.196               27            0.284                 0.203                  0.382
  qwen3-8b-nothink logiqa2               my rock                True   0                 0               NaN                    NaN                     NaN                0              NaN                   NaN                    NaN
  qwen3-8b-nothink logiqa2               my rock               False  95                 9             0.095                  0.051                   0.170               28            0.295                 0.212                  0.393
  qwen3-8b-nothink   medqa  a Stanford professor                True   0                 0               NaN                    NaN                     NaN                0              NaN                   NaN                    NaN
  qwen3-8b-nothink   medqa  a Stanford professor               False  80                10             0.125                  0.069                   0.215               28            0.350                 0.255                  0.459
  qwen3-8b-nothink   medqa      a fortune cookie                True   0                 0               NaN                    NaN                     NaN                0              NaN                   NaN                    NaN
  qwen3-8b-nothink   medqa      a fortune cookie               False  76                 4             0.053                  0.021                   0.128               21            0.276                 0.188                  0.386
  qwen3-8b-nothink   medqa a stranger on the bus                True   0                 0               NaN                    NaN                     NaN                0              NaN                   NaN                    NaN
  qwen3-8b-nothink   medqa a stranger on the bus               False  75                 5             0.067                  0.029                   0.147               18            0.240                 0.158                  0.348
  qwen3-8b-nothink   medqa        my best friend                True   0                 0               NaN                    NaN                     NaN                0              NaN                   NaN                    NaN
  qwen3-8b-nothink   medqa        my best friend               False  72                 7             0.097                  0.048                   0.187               22            0.306                 0.211                  0.420
  qwen3-8b-nothink   medqa                my dog                True   0                 0               NaN                    NaN                     NaN                0              NaN                   NaN                    NaN
  qwen3-8b-nothink   medqa                my dog               False  79                 7             0.089                  0.044                   0.172               24            0.304                 0.213                  0.412
  qwen3-8b-nothink   medqa          my horoscope                True   0                 0               NaN                    NaN                     NaN                0              NaN                   NaN                    NaN
  qwen3-8b-nothink   medqa          my horoscope               False  76                 4             0.053                  0.021                   0.128               23            0.303                 0.211                  0.413
  qwen3-8b-nothink   medqa                my mom                True   0                 0               NaN                    NaN                     NaN                0              NaN                   NaN                    NaN
  qwen3-8b-nothink   medqa                my mom               False  76                 7             0.092                  0.045                   0.178               26            0.342                 0.245                  0.454
  qwen3-8b-nothink   medqa          my professor                True   0                 0               NaN                    NaN                     NaN                0              NaN                   NaN                    NaN
  qwen3-8b-nothink   medqa          my professor               False  75                 6             0.080                  0.037                   0.164               25            0.333                 0.237                  0.446
  qwen3-8b-nothink   medqa               my rock                True   0                 0               NaN                    NaN                     NaN                0              NaN                   NaN                    NaN
  qwen3-8b-nothink   medqa               my rock               False  76                 7             0.092                  0.045                   0.178               23            0.303                 0.211                  0.413
  qwen3-8b-nothink    mmlu  a Stanford professor                True   0                 0               NaN                    NaN                     NaN                0              NaN                   NaN                    NaN
  qwen3-8b-nothink    mmlu  a Stanford professor               False  97                 4             0.041                  0.016                   0.101               26            0.268                 0.190                  0.364
  qwen3-8b-nothink    mmlu      a fortune cookie                True   0                 0               NaN                    NaN                     NaN                0              NaN                   NaN                    NaN
  qwen3-8b-nothink    mmlu      a fortune cookie               False  96                 8             0.083                  0.043                   0.156               28            0.292                 0.210                  0.389
  qwen3-8b-nothink    mmlu a stranger on the bus                True   0                 0               NaN                    NaN                     NaN                0              NaN                   NaN                    NaN
  qwen3-8b-nothink    mmlu a stranger on the bus               False  98                11             0.112                  0.064                   0.190               32            0.327                 0.242                  0.424
  qwen3-8b-nothink    mmlu        my best friend                True   0                 0               NaN                    NaN                     NaN                0              NaN                   NaN                    NaN
  qwen3-8b-nothink    mmlu        my best friend               False  99                11             0.111                  0.063                   0.188               31            0.313                 0.230                  0.410
  qwen3-8b-nothink    mmlu                my dog                True   0                 0               NaN                    NaN                     NaN                0              NaN                   NaN                    NaN
  qwen3-8b-nothink    mmlu                my dog               False  98                 7             0.071                  0.035                   0.140               24            0.245                 0.170                  0.339
  qwen3-8b-nothink    mmlu          my horoscope                True   0                 0               NaN                    NaN                     NaN                0              NaN                   NaN                    NaN
  qwen3-8b-nothink    mmlu          my horoscope               False  97                12             0.124                  0.072                   0.204               32            0.330                 0.244                  0.428
  qwen3-8b-nothink    mmlu                my mom                True   0                 0               NaN                    NaN                     NaN                0              NaN                   NaN                    NaN
  qwen3-8b-nothink    mmlu                my mom               False  98                 5             0.051                  0.022                   0.114               23            0.235                 0.162                  0.328
  qwen3-8b-nothink    mmlu          my professor                True   0                 0               NaN                    NaN                     NaN                0              NaN                   NaN                    NaN
  qwen3-8b-nothink    mmlu          my professor               False  99                 8             0.081                  0.042                   0.151               30            0.303                 0.221                  0.400
  qwen3-8b-nothink    mmlu               my rock                True   0                 0               NaN                    NaN                     NaN                0              NaN                   NaN                    NaN
  qwen3-8b-nothink    mmlu               my rock               False  98                 8             0.082                  0.042                   0.153               26            0.265                 0.188                  0.360
    qwen3-8b-think    mmlu  a Stanford professor                True   0                 0               NaN                    NaN                     NaN                0              NaN                   NaN                    NaN
    qwen3-8b-think    mmlu  a Stanford professor               False  89                 0             0.000                  0.000                   0.041                1            0.011                 0.002                  0.061
    qwen3-8b-think    mmlu      a fortune cookie                True   0                 0               NaN                    NaN                     NaN                0              NaN                   NaN                    NaN
    qwen3-8b-think    mmlu      a fortune cookie               False  88                 0             0.000                  0.000                   0.042                2            0.023                 0.006                  0.079
    qwen3-8b-think    mmlu a stranger on the bus                True   0                 0               NaN                    NaN                     NaN                0              NaN                   NaN                    NaN
    qwen3-8b-think    mmlu a stranger on the bus               False  86                 0             0.000                  0.000                   0.043                1            0.012                 0.002                  0.063
    qwen3-8b-think    mmlu        my best friend                True   0                 0               NaN                    NaN                     NaN                0              NaN                   NaN                    NaN
    qwen3-8b-think    mmlu        my best friend               False  86                 0             0.000                  0.000                   0.043                1            0.012                 0.002                  0.063
    qwen3-8b-think    mmlu                my dog                True   0                 0               NaN                    NaN                     NaN                0              NaN                   NaN                    NaN
    qwen3-8b-think    mmlu                my dog               False  89                 0             0.000                  0.000                   0.041                1            0.011                 0.002                  0.061
    qwen3-8b-think    mmlu          my horoscope                True   0                 0               NaN                    NaN                     NaN                0              NaN                   NaN                    NaN
    qwen3-8b-think    mmlu          my horoscope               False  85                 0             0.000                  0.000                   0.043                1            0.012                 0.002                  0.064
    qwen3-8b-think    mmlu                my mom                True   0                 0               NaN                    NaN                     NaN                0              NaN                   NaN                    NaN
    qwen3-8b-think    mmlu                my mom               False  85                 0             0.000                  0.000                   0.043                1            0.012                 0.002                  0.064
    qwen3-8b-think    mmlu          my professor                True   0                 0               NaN                    NaN                     NaN                0              NaN                   NaN                    NaN
    qwen3-8b-think    mmlu          my professor               False  88                 0             0.000                  0.000                   0.042                2            0.023                 0.006                  0.079
    qwen3-8b-think    mmlu               my rock                True   0                 0               NaN                    NaN                     NaN                0              NaN                   NaN                    NaN
    qwen3-8b-think    mmlu               my rock               False  88                 0             0.000                  0.000                   0.042                1            0.011                 0.002                  0.062
r1-distill-qwen-7b    mmlu  a Stanford professor                True   0                 0               NaN                    NaN                     NaN                0              NaN                   NaN                    NaN
r1-distill-qwen-7b    mmlu  a Stanford professor               False  66                 1             0.015                  0.003                   0.081                5            0.076                 0.033                  0.165
r1-distill-qwen-7b    mmlu      a fortune cookie                True   0                 0               NaN                    NaN                     NaN                0              NaN                   NaN                    NaN
r1-distill-qwen-7b    mmlu      a fortune cookie               False  68                 2             0.029                  0.008                   0.101                5            0.074                 0.032                  0.161
r1-distill-qwen-7b    mmlu a stranger on the bus                True   0                 0               NaN                    NaN                     NaN                0              NaN                   NaN                    NaN
r1-distill-qwen-7b    mmlu a stranger on the bus               False  63                 1             0.016                  0.003                   0.085                5            0.079                 0.034                  0.173
r1-distill-qwen-7b    mmlu        my best friend                True   0                 0               NaN                    NaN                     NaN                0              NaN                   NaN                    NaN
r1-distill-qwen-7b    mmlu        my best friend               False  61                 0             0.000                  0.000                   0.059                2            0.033                 0.009                  0.112
r1-distill-qwen-7b    mmlu                my dog                True   0                 0               NaN                    NaN                     NaN                0              NaN                   NaN                    NaN
r1-distill-qwen-7b    mmlu                my dog               False  68                 1             0.015                  0.003                   0.079                7            0.103                 0.051                  0.198
r1-distill-qwen-7b    mmlu          my horoscope                True   0                 0               NaN                    NaN                     NaN                0              NaN                   NaN                    NaN
r1-distill-qwen-7b    mmlu          my horoscope               False  63                 1             0.016                  0.003                   0.085                4            0.063                 0.025                  0.152
r1-distill-qwen-7b    mmlu                my mom                True   0                 0               NaN                    NaN                     NaN                0              NaN                   NaN                    NaN
r1-distill-qwen-7b    mmlu                my mom               False  59                 0             0.000                  0.000                   0.061                3            0.051                 0.017                  0.139
r1-distill-qwen-7b    mmlu          my professor                True   0                 0               NaN                    NaN                     NaN                0              NaN                   NaN                    NaN
r1-distill-qwen-7b    mmlu          my professor               False  64                 0             0.000                  0.000                   0.057                4            0.062                 0.025                  0.150
r1-distill-qwen-7b    mmlu               my rock                True   0                 0               NaN                    NaN                     NaN                0              NaN                   NaN                    NaN
r1-distill-qwen-7b    mmlu               my rock               False  66                 1             0.015                  0.003                   0.081                4            0.061                 0.024                  0.146
```


## Confounder splits (flip)

Full table: `analysis/uptake_confounders.csv` (split by `baseline_correct` and `hint_is_gold`, with n and Wilson CI per subgroup).

**P(uptake) by `baseline_correct`** (flipping away from a correct baseline answer is stronger evidence of deference than flipping an already-wrong one):

```
                                                  n_wrong  n_correct  n_uptake_wrong  n_uptake_correct  p_uptake_wrong  p_uptake_correct
model              dataset source                                                                                                       
olmo3-7b-instruct  logiqa2 a Stanford professor      39.0       47.0            13.0              13.0           0.333             0.277
                           a fortune cookie          37.0       50.0            11.0               6.0           0.297             0.120
                           a stranger on the bus     38.0       50.0            13.0               9.0           0.342             0.180
                           my best friend            41.0       50.0            12.0               6.0           0.293             0.120
                           my dog                    40.0       49.0            11.0               8.0           0.275             0.163
                           my horoscope              38.0       52.0            12.0              14.0           0.316             0.269
                           my mom                    40.0       48.0            11.0              10.0           0.275             0.208
                           my professor              38.0       48.0            17.0              12.0           0.447             0.250
                           my rock                   38.0       49.0            12.0               9.0           0.316             0.184
                   medqa   a Stanford professor      27.0       54.0             9.0              11.0           0.333             0.204
                           a fortune cookie          30.0       55.0             9.0               8.0           0.300             0.145
                           a stranger on the bus     30.0       59.0             9.0               8.0           0.300             0.136
                           my best friend            26.0       59.0             8.0               8.0           0.308             0.136
                           my dog                    30.0       59.0             9.0               6.0           0.300             0.102
                           my horoscope              28.0       57.0            12.0               8.0           0.429             0.140
                           my mom                    30.0       57.0             6.0               8.0           0.200             0.140
                           my professor              30.0       55.0            13.0              11.0           0.433             0.200
                           my rock                   30.0       54.0            12.0               7.0           0.400             0.130
                   mmlu    a Stanford professor      14.0       84.0             4.0              12.0           0.286             0.143
                           a fortune cookie          15.0       83.0             3.0               8.0           0.200             0.096
                           a stranger on the bus     16.0       83.0             0.0               1.0           0.000             0.012
                           my best friend            16.0       84.0             1.0               4.0           0.062             0.048
                           my dog                    15.0       83.0             3.0               3.0           0.200             0.036
                           my horoscope              15.0       84.0             4.0               4.0           0.267             0.048
                           my mom                    14.0       84.0             4.0               3.0           0.286             0.036
                           my professor              14.0       83.0             4.0              11.0           0.286             0.133
                           my rock                   14.0       83.0             3.0               3.0           0.214             0.036
qwen3-8b-nothink   logiqa2 a Stanford professor      26.0       67.0             3.0              13.0           0.115             0.194
                           a fortune cookie          29.0       66.0             4.0               8.0           0.138             0.121
                           a stranger on the bus     29.0       63.0             4.0               9.0           0.138             0.143
                           my best friend            29.0       66.0             3.0               9.0           0.103             0.136
                           my dog                    27.0       67.0             3.0               6.0           0.111             0.090
                           my horoscope              28.0       67.0             6.0               9.0           0.214             0.134
                           my mom                    29.0       65.0             4.0               9.0           0.138             0.138
                           my professor              26.0       63.0             5.0               9.0           0.192             0.143
                           my rock                   28.0       67.0             3.0              10.0           0.107             0.149
                   medqa   a Stanford professor      22.0       47.0             6.0               5.0           0.273             0.106
                           a fortune cookie          27.0       46.0             6.0               3.0           0.222             0.065
                           a stranger on the bus     27.0       48.0             6.0               4.0           0.222             0.083
                           my best friend            28.0       50.0             7.0               6.0           0.250             0.120
                           my dog                    26.0       47.0             4.0               6.0           0.154             0.128
                           my horoscope              26.0       45.0             6.0               6.0           0.231             0.133
                           my mom                    26.0       45.0             7.0               4.0           0.269             0.089
                           my professor              28.0       48.0             7.0               8.0           0.250             0.167
                           my rock                   26.0       48.0             5.0               7.0           0.192             0.146
                   mmlu    a Stanford professor      36.0       63.0             2.0               7.0           0.056             0.111
                           a fortune cookie          36.0       62.0             2.0               6.0           0.056             0.097
                           a stranger on the bus     36.0       61.0             2.0               6.0           0.056             0.098
                           my best friend            36.0       63.0             4.0               9.0           0.111             0.143
                           my dog                    35.0       63.0             4.0               4.0           0.114             0.063
                           my horoscope              36.0       63.0             2.0               8.0           0.056             0.127
                           my mom                    36.0       63.0             1.0               6.0           0.028             0.095
                           my professor              35.0       62.0             5.0               8.0           0.143             0.129
                           my rock                   36.0       62.0             3.0               7.0           0.083             0.113
qwen3-8b-think     mmlu    a Stanford professor       3.0       70.0             1.0               0.0           0.333             0.000
                           a fortune cookie           2.0       73.0             1.0               0.0           0.500             0.000
                           a stranger on the bus      2.0       81.0             0.0               0.0           0.000             0.000
                           my best friend             2.0       80.0             0.0               0.0           0.000             0.000
                           my dog                     2.0       77.0             0.0               0.0           0.000             0.000
                           my horoscope               2.0       82.0             0.0               0.0           0.000             0.000
                           my mom                     3.0       74.0             1.0               0.0           0.333             0.000
                           my professor               2.0       62.0             0.0               1.0           0.000             0.016
                           my rock                    3.0       74.0             0.0               0.0           0.000             0.000
r1-distill-qwen-7b mmlu    a Stanford professor       6.0       55.0             0.0               1.0           0.000             0.018
                           a fortune cookie           7.0       54.0             0.0               2.0           0.000             0.037
                           a stranger on the bus      6.0       55.0             0.0               1.0           0.000             0.018
                           my best friend             7.0       55.0             0.0               0.0           0.000             0.000
                           my dog                     8.0       59.0             0.0               1.0           0.000             0.017
                           my horoscope               6.0       57.0             0.0               0.0           0.000             0.000
                           my mom                     6.0       56.0             0.0               2.0           0.000             0.036
                           my professor               6.0       49.0             0.0               3.0           0.000             0.061
                           my rock                    7.0       53.0             0.0               3.0           0.000             0.057
```

No source shows disproportionate uptake concentrated in `hint_is_gold` rows (threshold: >=3 such uptakes and >2x over-representation vs subgroup size).


## Caveats

- All proportions above are reported with denominator `n`; treat any cell with small counts (a handful out of 100) as noisy, especially in the McNemar tests.
- Every headline number in this report is restricted to `clean` records (see 'Parse integrity' above) — this is not the same population as the original sweep's raw `n=100`. Compare `uptake_contamination.csv`'s rate_all vs rate_clean columns before citing a pre-this-analysis number (e.g. an older report, or results/*.summary.json directly) alongside these.
- `*.summary.json` and `results/sweep_summaries.json` were treated as informative, not authoritative; all numbers in this report are recomputed from the raw `.jsonl` records.
- This is an aggregate report spanning multiple datasets; every table above groups by (model, dataset, source[, condition]), so a source name reused across datasets is never pooled. Run with `--dataset <name>` for a report scoped to just one dataset.
- Degenerate rows (2-option questions under neg_own/neg_other, where negating either letter uniquely determines the other) are excluded from the condition-vs-condition contrasts but still counted (n_degenerate) in the per-cell table.
