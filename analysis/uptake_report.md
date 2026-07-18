# Uptake analysis report

Generated from `results` (1 model(s), 8 source(s) observed).

## Missing cells

No missing flip cells among observed model x source combinations.

**Missing placebo cells (1):** olmo3-7b-instruct/my horoscope


## Sanity checks

- Multi-source flip/placebo cells (should be 0): 0
- Baseline-answer mismatches within a model across cells (should be 0): 0 idx affected
- Recomputed-vs-stored uptake mismatches (should be 0): 0
- Recomputed-vs-summary.json discrepancies (should be 0): 0
- Null `baseline_answer` rows excluded from denominators, by cell: none
- `n_options_context` is not recorded per-record; all observed answer letters are within A-D across the full dataset, so it is fixed at 4 for every row.

## Per-cell effectiveness table

Full table: `analysis/uptake_table.csv`. P(uptake) with 95% Wilson CI, n and n_uptake shown; `p_answer_changed` is the placebo-condition churn rate (noise floor).

```
            model                source   n  n_uptake  p_uptake  ci_low  ci_high  n_placebo  p_answer_changed  n_excluded_null_baseline
olmo3-7b-instruct  a Stanford professor 100        17      0.17   0.109    0.255      100.0              0.07                         0
olmo3-7b-instruct a stranger on the bus 100         4      0.04   0.016    0.098      100.0              0.09                         0
olmo3-7b-instruct        my best friend 100        10      0.10   0.055    0.174      100.0              0.08                         0
olmo3-7b-instruct                my dog 100         6      0.06   0.028    0.125      100.0              0.08                         0
olmo3-7b-instruct          my horoscope 100         8      0.08   0.041    0.150        NaN               NaN                         0
olmo3-7b-instruct                my mom 100        11      0.11   0.063    0.186      100.0              0.05                         0
olmo3-7b-instruct          my professor 100        15      0.15   0.093    0.233      100.0              0.04                         0
olmo3-7b-instruct               my rock 100         6      0.06   0.028    0.125      100.0              0.10                         0
```

**High placebo churn (> 5%):** cells where agreeing hints still destabilize the answer; treat flip-condition uptake there as inflated by noise.

  - olmo3-7b-instruct / a Stanford professor: p_answer_changed=7.0% (n=100)
  - olmo3-7b-instruct / a stranger on the bus: p_answer_changed=9.0% (n=100)
  - olmo3-7b-instruct / my best friend: p_answer_changed=8.0% (n=100)
  - olmo3-7b-instruct / my dog: p_answer_changed=8.0% (n=100)
  - olmo3-7b-instruct / my rock: p_answer_changed=10.0% (n=100)

## Effectiveness ordering & cross-model consistency

![Uptake heatmap](uptake_heatmap.png)

Sources ordered by mean P(uptake) across models (descending), used as heatmap column order: ['a Stanford professor', 'my professor', 'my mom', 'my best friend', 'my horoscope', 'my dog', 'my rock', 'a stranger on the bus']

Only one model is present in the current results, so Kendall's tau against the cross-model mean ranking is degenerate (a model compared against a ranking built from itself) and not informative yet. Re-run once more models are swept.

Per-model tau vs cross-model mean ranking:

```
            model  n_sources  tau_vs_mean_ranking
olmo3-7b-instruct          8                  1.0
```


## Paired significance (McNemar, Holm-corrected within model)

Full pairwise table: `analysis/uptake_pairwise.csv`. Highlights below: top-vs-bottom source per model, and `a Stanford professor` vs every other source.

**olmo3-7b-instruct** (top source: a Stanford professor, bottom source: a stranger on the bus)

```
            source_a              source_b  n_paired  b_a_only  c_b_only  p_value  p_holm
a Stanford professor a stranger on the bus       100        16         3   0.0044  0.1195
a Stanford professor               my rock       100        13         2   0.0074  0.1920
a Stanford professor                my dog       100        16         5   0.0266  0.5853
a Stanford professor        my best friend       100        11         4   0.1185  1.0000
a Stanford professor          my horoscope       100        14         5   0.0636  1.0000
a Stanford professor                my mom       100        13         7   0.2632  1.0000
a Stanford professor          my professor       100         9         7   0.8036  1.0000
```

_statsmodels not installed — skipping the clustered logistic-regression cross-check (McNemar results above stand on their own)._


## Confounder splits

Full table: `analysis/uptake_confounders.csv` (split by `baseline_correct` and `hint_is_gold`, with n and Wilson CI per subgroup).

**P(uptake) by `baseline_correct`** (flipping away from a correct baseline answer is stronger evidence of deference than flipping an already-wrong one):

```
                                         n_wrong  n_correct  n_uptake_wrong  n_uptake_correct  p_uptake_wrong  p_uptake_correct
model             source                                                                                                       
olmo3-7b-instruct a Stanford professor      16.0       84.0             4.0              13.0           0.250             0.155
                  a stranger on the bus     16.0       84.0             3.0               1.0           0.188             0.012
                  my best friend            16.0       84.0             6.0               4.0           0.375             0.048
                  my dog                    16.0       84.0             5.0               1.0           0.312             0.012
                  my horoscope              16.0       84.0             5.0               3.0           0.312             0.036
                  my mom                    16.0       84.0             7.0               4.0           0.438             0.048
                  my professor              16.0       84.0             7.0               8.0           0.438             0.095
                  my rock                   16.0       84.0             4.0               2.0           0.250             0.024
```

**Sources where `hint_is_gold` cases are over-represented among uptakes** (uptake there may reflect re-solving toward the correct answer rather than pure deference to the source):

  - olmo3-7b-instruct / my best friend: 4/10 uptakes (40%) come from hint_is_gold rows, which are only 5% of that cell's data.
  - olmo3-7b-instruct / my mom: 3/11 uptakes (27%) come from hint_is_gold rows, which are only 5% of that cell's data.
  - olmo3-7b-instruct / my professor: 4/15 uptakes (27%) come from hint_is_gold rows, which are only 5% of that cell's data.

## Caveats

- All proportions above are reported with denominator `n`; treat any cell with small `n_uptake` (a handful of flips out of 100) as noisy, especially in the McNemar tests.
- `results/*.summary.json` and `results/sweep_summaries.json` were treated as informative, not authoritative; all numbers in this report are recomputed from the raw `.jsonl` records.
- `results/sweep_summaries.json` does not exist in this run of the sweep; only the per-file `*.summary.json` aggregates were available for cross-checking.
