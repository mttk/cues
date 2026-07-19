# Uptake analysis report

Generated from `results` (5 model(s), 9 source(s) observed, dataset(s): ['mmlu']).

## Missing cells

No missing flip cells among observed model x source combinations.

No missing placebo cells among observed model x source combinations.


## Sanity checks

- Multi-source flip/placebo cells (should be 0): 0
- Baseline-answer mismatches within a model across cells (should be 0): 0 idx affected
- Recomputed-vs-stored uptake mismatches (should be 0): 0
- Recomputed-vs-summary.json discrepancies (should be 0): 27
  - {'model': 'olmo3-7b-think', 'source': 'a Stanford professor', 'summary_n': 100, 'recomputed_n': 93, 'summary_n_uptake': 20, 'recomputed_n_uptake': 20}
  - {'model': 'olmo3-7b-think', 'source': 'a fortune cookie', 'summary_n': 100, 'recomputed_n': 93, 'summary_n_uptake': 22, 'recomputed_n_uptake': 18}
  - {'model': 'olmo3-7b-think', 'source': 'a stranger on the bus', 'summary_n': 100, 'recomputed_n': 93, 'summary_n_uptake': 11, 'recomputed_n_uptake': 10}
  - {'model': 'olmo3-7b-think', 'source': 'my best friend', 'summary_n': 100, 'recomputed_n': 93, 'summary_n_uptake': 12, 'recomputed_n_uptake': 12}
  - {'model': 'olmo3-7b-think', 'source': 'my dog', 'summary_n': 100, 'recomputed_n': 93, 'summary_n_uptake': 13, 'recomputed_n_uptake': 12}
  - {'model': 'olmo3-7b-think', 'source': 'my horoscope', 'summary_n': 100, 'recomputed_n': 93, 'summary_n_uptake': 8, 'recomputed_n_uptake': 8}
  - {'model': 'olmo3-7b-think', 'source': 'my mom', 'summary_n': 100, 'recomputed_n': 93, 'summary_n_uptake': 13, 'recomputed_n_uptake': 13}
  - {'model': 'olmo3-7b-think', 'source': 'my professor', 'summary_n': 100, 'recomputed_n': 93, 'summary_n_uptake': 14, 'recomputed_n_uptake': 11}
  - {'model': 'olmo3-7b-think', 'source': 'my rock', 'summary_n': 100, 'recomputed_n': 93, 'summary_n_uptake': 16, 'recomputed_n_uptake': 15}
  - {'model': 'qwen3-8b-think', 'source': 'a Stanford professor', 'summary_n': 100, 'recomputed_n': 95, 'summary_n_uptake': 17, 'recomputed_n_uptake': 16}
  - {'model': 'qwen3-8b-think', 'source': 'a fortune cookie', 'summary_n': 100, 'recomputed_n': 95, 'summary_n_uptake': 4, 'recomputed_n_uptake': 4}
  - {'model': 'qwen3-8b-think', 'source': 'a stranger on the bus', 'summary_n': 100, 'recomputed_n': 95, 'summary_n_uptake': 6, 'recomputed_n_uptake': 6}
  - {'model': 'qwen3-8b-think', 'source': 'my best friend', 'summary_n': 100, 'recomputed_n': 95, 'summary_n_uptake': 3, 'recomputed_n_uptake': 3}
  - {'model': 'qwen3-8b-think', 'source': 'my dog', 'summary_n': 100, 'recomputed_n': 95, 'summary_n_uptake': 3, 'recomputed_n_uptake': 3}
  - {'model': 'qwen3-8b-think', 'source': 'my horoscope', 'summary_n': 100, 'recomputed_n': 95, 'summary_n_uptake': 6, 'recomputed_n_uptake': 6}
  - {'model': 'qwen3-8b-think', 'source': 'my mom', 'summary_n': 100, 'recomputed_n': 95, 'summary_n_uptake': 8, 'recomputed_n_uptake': 7}
  - {'model': 'qwen3-8b-think', 'source': 'my professor', 'summary_n': 100, 'recomputed_n': 95, 'summary_n_uptake': 14, 'recomputed_n_uptake': 13}
  - {'model': 'qwen3-8b-think', 'source': 'my rock', 'summary_n': 100, 'recomputed_n': 95, 'summary_n_uptake': 7, 'recomputed_n_uptake': 6}
  - {'model': 'r1-distill-qwen-7b', 'source': 'a Stanford professor', 'summary_n': 100, 'recomputed_n': 89, 'summary_n_uptake': 11, 'recomputed_n_uptake': 8}
  - {'model': 'r1-distill-qwen-7b', 'source': 'a fortune cookie', 'summary_n': 100, 'recomputed_n': 89, 'summary_n_uptake': 12, 'recomputed_n_uptake': 10}
  - {'model': 'r1-distill-qwen-7b', 'source': 'a stranger on the bus', 'summary_n': 100, 'recomputed_n': 89, 'summary_n_uptake': 13, 'recomputed_n_uptake': 6}
  - {'model': 'r1-distill-qwen-7b', 'source': 'my best friend', 'summary_n': 100, 'recomputed_n': 89, 'summary_n_uptake': 6, 'recomputed_n_uptake': 4}
  - {'model': 'r1-distill-qwen-7b', 'source': 'my dog', 'summary_n': 100, 'recomputed_n': 89, 'summary_n_uptake': 9, 'recomputed_n_uptake': 6}
  - {'model': 'r1-distill-qwen-7b', 'source': 'my horoscope', 'summary_n': 100, 'recomputed_n': 89, 'summary_n_uptake': 14, 'recomputed_n_uptake': 11}
  - {'model': 'r1-distill-qwen-7b', 'source': 'my mom', 'summary_n': 100, 'recomputed_n': 89, 'summary_n_uptake': 10, 'recomputed_n_uptake': 8}
  - {'model': 'r1-distill-qwen-7b', 'source': 'my professor', 'summary_n': 100, 'recomputed_n': 89, 'summary_n_uptake': 18, 'recomputed_n_uptake': 14}
  - {'model': 'r1-distill-qwen-7b', 'source': 'my rock', 'summary_n': 100, 'recomputed_n': 89, 'summary_n_uptake': 10, 'recomputed_n_uptake': 7}
- Null `baseline_answer` rows excluded from denominators, by cell: {('olmo3-7b-think', 'a Stanford professor'): np.int64(7), ('olmo3-7b-think', 'a fortune cookie'): np.int64(7), ('olmo3-7b-think', 'a stranger on the bus'): np.int64(7), ('olmo3-7b-think', 'my best friend'): np.int64(7), ('olmo3-7b-think', 'my dog'): np.int64(7), ('olmo3-7b-think', 'my horoscope'): np.int64(7), ('olmo3-7b-think', 'my mom'): np.int64(7), ('olmo3-7b-think', 'my professor'): np.int64(7), ('olmo3-7b-think', 'my rock'): np.int64(7), ('qwen3-8b-think', 'a Stanford professor'): np.int64(5), ('qwen3-8b-think', 'a fortune cookie'): np.int64(5), ('qwen3-8b-think', 'a stranger on the bus'): np.int64(5), ('qwen3-8b-think', 'my best friend'): np.int64(5), ('qwen3-8b-think', 'my dog'): np.int64(5), ('qwen3-8b-think', 'my horoscope'): np.int64(5), ('qwen3-8b-think', 'my mom'): np.int64(5), ('qwen3-8b-think', 'my professor'): np.int64(5), ('qwen3-8b-think', 'my rock'): np.int64(5), ('r1-distill-qwen-7b', 'a Stanford professor'): np.int64(11), ('r1-distill-qwen-7b', 'a fortune cookie'): np.int64(11), ('r1-distill-qwen-7b', 'a stranger on the bus'): np.int64(11), ('r1-distill-qwen-7b', 'my best friend'): np.int64(11), ('r1-distill-qwen-7b', 'my dog'): np.int64(11), ('r1-distill-qwen-7b', 'my horoscope'): np.int64(11), ('r1-distill-qwen-7b', 'my mom'): np.int64(11), ('r1-distill-qwen-7b', 'my professor'): np.int64(11), ('r1-distill-qwen-7b', 'my rock'): np.int64(11)}
- `n_options_context` is not recorded per-record; all observed answer letters are within A-D across the full dataset, so it is fixed at 4 for every row.

## Per-cell effectiveness table

Full table: `analysis/uptake_table.csv`. P(uptake) with 95% Wilson CI, n and n_uptake shown; `p_answer_changed` is the placebo-condition churn rate (noise floor).

```
             model                source   n  n_uptake  p_uptake  ci_low  ci_high  n_placebo  p_answer_changed  n_excluded_null_baseline
 olmo3-7b-instruct  a Stanford professor 100        17     0.170   0.109    0.255        100             0.070                         0
 olmo3-7b-instruct      a fortune cookie 100         4     0.040   0.016    0.098        100             0.070                         0
 olmo3-7b-instruct a stranger on the bus 100         4     0.040   0.016    0.098        100             0.090                         0
 olmo3-7b-instruct        my best friend 100        10     0.100   0.055    0.174        100             0.080                         0
 olmo3-7b-instruct                my dog 100         6     0.060   0.028    0.125        100             0.080                         0
 olmo3-7b-instruct          my horoscope 100         8     0.080   0.041    0.150        100             0.050                         0
 olmo3-7b-instruct                my mom 100        11     0.110   0.063    0.186        100             0.050                         0
 olmo3-7b-instruct          my professor 100        15     0.150   0.093    0.233        100             0.040                         0
 olmo3-7b-instruct               my rock 100         6     0.060   0.028    0.125        100             0.100                         0
    olmo3-7b-think  a Stanford professor  93        20     0.215   0.144    0.309         93             0.161                         7
    olmo3-7b-think      a fortune cookie  93        18     0.194   0.126    0.285         93             0.097                         7
    olmo3-7b-think a stranger on the bus  93        10     0.108   0.059    0.187         93             0.183                         7
    olmo3-7b-think        my best friend  93        12     0.129   0.075    0.212         93             0.161                         7
    olmo3-7b-think                my dog  93        12     0.129   0.075    0.212         93             0.108                         7
    olmo3-7b-think          my horoscope  93         8     0.086   0.044    0.161         93             0.129                         7
    olmo3-7b-think                my mom  93        13     0.140   0.084    0.225         93             0.183                         7
    olmo3-7b-think          my professor  93        11     0.118   0.067    0.199         93             0.118                         7
    olmo3-7b-think               my rock  93        15     0.161   0.100    0.249         93             0.172                         7
  qwen3-8b-nothink  a Stanford professor 100        14     0.140   0.085    0.221        100             0.270                         0
  qwen3-8b-nothink      a fortune cookie 100        12     0.120   0.070    0.198        100             0.270                         0
  qwen3-8b-nothink a stranger on the bus 100        13     0.130   0.078    0.210        100             0.210                         0
  qwen3-8b-nothink        my best friend 100        11     0.110   0.063    0.186        100             0.240                         0
  qwen3-8b-nothink                my dog 100        10     0.100   0.055    0.174        100             0.190                         0
  qwen3-8b-nothink          my horoscope 100        13     0.130   0.078    0.210        100             0.230                         0
  qwen3-8b-nothink                my mom 100        12     0.120   0.070    0.198        100             0.240                         0
  qwen3-8b-nothink          my professor 100        15     0.150   0.093    0.233        100             0.280                         0
  qwen3-8b-nothink               my rock 100         9     0.090   0.048    0.162        100             0.230                         0
    qwen3-8b-think  a Stanford professor  95        16     0.168   0.106    0.256         95             0.021                         5
    qwen3-8b-think      a fortune cookie  95         4     0.042   0.016    0.103         95             0.021                         5
    qwen3-8b-think a stranger on the bus  95         6     0.063   0.029    0.131         95             0.011                         5
    qwen3-8b-think        my best friend  95         3     0.032   0.011    0.089         95             0.042                         5
    qwen3-8b-think                my dog  95         3     0.032   0.011    0.089         95             0.021                         5
    qwen3-8b-think          my horoscope  95         6     0.063   0.029    0.131         95             0.032                         5
    qwen3-8b-think                my mom  95         7     0.074   0.036    0.144         95             0.032                         5
    qwen3-8b-think          my professor  95        13     0.137   0.082    0.220         95             0.042                         5
    qwen3-8b-think               my rock  95         6     0.063   0.029    0.131         95             0.021                         5
r1-distill-qwen-7b  a Stanford professor  89         8     0.090   0.046    0.167         89             0.180                        11
r1-distill-qwen-7b      a fortune cookie  89        10     0.112   0.062    0.195         89             0.202                        11
r1-distill-qwen-7b a stranger on the bus  89         6     0.067   0.031    0.139         89             0.157                        11
r1-distill-qwen-7b        my best friend  89         4     0.045   0.018    0.110         89             0.157                        11
r1-distill-qwen-7b                my dog  89         6     0.067   0.031    0.139         89             0.202                        11
r1-distill-qwen-7b          my horoscope  89        11     0.124   0.070    0.208         89             0.202                        11
r1-distill-qwen-7b                my mom  89         8     0.090   0.046    0.167         89             0.202                        11
r1-distill-qwen-7b          my professor  89        14     0.157   0.096    0.247         89             0.112                        11
r1-distill-qwen-7b               my rock  89         7     0.079   0.039    0.154         89             0.124                        11
```

**High placebo churn (> 5%):** cells where agreeing hints still destabilize the answer; treat flip-condition uptake there as inflated by noise.

  - olmo3-7b-instruct / a Stanford professor: p_answer_changed=7.0% (n=100)
  - olmo3-7b-instruct / a fortune cookie: p_answer_changed=7.0% (n=100)
  - olmo3-7b-instruct / a stranger on the bus: p_answer_changed=9.0% (n=100)
  - olmo3-7b-instruct / my best friend: p_answer_changed=8.0% (n=100)
  - olmo3-7b-instruct / my dog: p_answer_changed=8.0% (n=100)
  - olmo3-7b-instruct / my rock: p_answer_changed=10.0% (n=100)
  - olmo3-7b-think / a Stanford professor: p_answer_changed=16.1% (n=93)
  - olmo3-7b-think / a fortune cookie: p_answer_changed=9.7% (n=93)
  - olmo3-7b-think / a stranger on the bus: p_answer_changed=18.3% (n=93)
  - olmo3-7b-think / my best friend: p_answer_changed=16.1% (n=93)
  - olmo3-7b-think / my dog: p_answer_changed=10.8% (n=93)
  - olmo3-7b-think / my horoscope: p_answer_changed=12.9% (n=93)
  - olmo3-7b-think / my mom: p_answer_changed=18.3% (n=93)
  - olmo3-7b-think / my professor: p_answer_changed=11.8% (n=93)
  - olmo3-7b-think / my rock: p_answer_changed=17.2% (n=93)
  - qwen3-8b-nothink / a Stanford professor: p_answer_changed=27.0% (n=100)
  - qwen3-8b-nothink / a fortune cookie: p_answer_changed=27.0% (n=100)
  - qwen3-8b-nothink / a stranger on the bus: p_answer_changed=21.0% (n=100)
  - qwen3-8b-nothink / my best friend: p_answer_changed=24.0% (n=100)
  - qwen3-8b-nothink / my dog: p_answer_changed=19.0% (n=100)
  - qwen3-8b-nothink / my horoscope: p_answer_changed=23.0% (n=100)
  - qwen3-8b-nothink / my mom: p_answer_changed=24.0% (n=100)
  - qwen3-8b-nothink / my professor: p_answer_changed=28.0% (n=100)
  - qwen3-8b-nothink / my rock: p_answer_changed=23.0% (n=100)
  - r1-distill-qwen-7b / a Stanford professor: p_answer_changed=18.0% (n=89)
  - r1-distill-qwen-7b / a fortune cookie: p_answer_changed=20.2% (n=89)
  - r1-distill-qwen-7b / a stranger on the bus: p_answer_changed=15.7% (n=89)
  - r1-distill-qwen-7b / my best friend: p_answer_changed=15.7% (n=89)
  - r1-distill-qwen-7b / my dog: p_answer_changed=20.2% (n=89)
  - r1-distill-qwen-7b / my horoscope: p_answer_changed=20.2% (n=89)
  - r1-distill-qwen-7b / my mom: p_answer_changed=20.2% (n=89)
  - r1-distill-qwen-7b / my professor: p_answer_changed=11.2% (n=89)
  - r1-distill-qwen-7b / my rock: p_answer_changed=12.4% (n=89)

## Effectiveness ordering & cross-model consistency

![Uptake heatmap](uptake_heatmap.png)

Sources ordered by mean P(uptake) across models (descending), used as heatmap column order: ['a Stanford professor', 'my professor', 'my mom', 'a fortune cookie', 'my horoscope', 'my rock', 'my best friend', 'a stranger on the bus', 'my dog']

Per-model tau vs cross-model mean ranking:

```
             model  n_sources  tau_vs_mean_ranking
 olmo3-7b-instruct          9                0.572
    olmo3-7b-think          9                0.310
  qwen3-8b-nothink          9                0.457
    qwen3-8b-think          9                0.707
r1-distill-qwen-7b          9                0.514
```


## Paired significance (McNemar, Holm-corrected within model)

Full pairwise table: `analysis/uptake_pairwise.csv`. Highlights below: top-vs-bottom source per model, and `a Stanford professor` vs every other source.

**olmo3-7b-instruct** (top source: a Stanford professor, bottom source: a fortune cookie)

```
            source_a              source_b  n_paired  b_a_only  c_b_only  p_value  p_holm
a Stanford professor      a fortune cookie       100        13         0   0.0002  0.0088
a Stanford professor a stranger on the bus       100        16         3   0.0044  0.1460
a Stanford professor               my rock       100        13         2   0.0074  0.2363
a Stanford professor                my dog       100        16         5   0.0266  0.7449
a Stanford professor        my best friend       100        11         4   0.1185  1.0000
a Stanford professor          my horoscope       100        14         5   0.0636  1.0000
a Stanford professor                my mom       100        13         7   0.2632  1.0000
a Stanford professor          my professor       100         9         7   0.8036  1.0000
```

**olmo3-7b-think** (top source: a Stanford professor, bottom source: my horoscope)

```
            source_a              source_b  n_paired  b_a_only  c_b_only  p_value  p_holm
a Stanford professor          my horoscope        93        18         6   0.0227  0.8156
a Stanford professor      a fortune cookie        93        11         9   0.8238  1.0000
a Stanford professor a stranger on the bus        93        14         4   0.0309  1.0000
a Stanford professor        my best friend        93        17         9   0.1686  1.0000
a Stanford professor                my dog        93        14         6   0.1153  1.0000
a Stanford professor                my mom        93        14         7   0.1892  1.0000
a Stanford professor          my professor        93        15         6   0.0784  1.0000
a Stanford professor               my rock        93        15        10   0.4244  1.0000
```

**qwen3-8b-nothink** (top source: my professor, bottom source: my rock)

```
            source_a              source_b  n_paired  b_a_only  c_b_only  p_value  p_holm
        my professor               my rock       100         9         3   0.1460     1.0
a Stanford professor      a fortune cookie       100         5         3   0.7266     1.0
a Stanford professor a stranger on the bus       100         6         5   1.0000     1.0
a Stanford professor        my best friend       100         8         5   0.5811     1.0
a Stanford professor                my dog       100         9         5   0.4240     1.0
a Stanford professor          my horoscope       100         8         7   1.0000     1.0
a Stanford professor                my mom       100         8         6   0.7905     1.0
a Stanford professor          my professor       100         7         8   1.0000     1.0
a Stanford professor               my rock       100        10         5   0.3018     1.0
```

**qwen3-8b-think** (top source: a Stanford professor, bottom source: my best friend)

```
            source_a              source_b  n_paired  b_a_only  c_b_only  p_value  p_holm
a Stanford professor        my best friend        95        13         0   0.0002  0.0088
a Stanford professor                my dog        95        14         1   0.0010  0.0342
a Stanford professor      a fortune cookie        95        14         2   0.0042  0.1338
a Stanford professor          my horoscope        95        11         1   0.0063  0.1968
a Stanford professor a stranger on the bus        95        12         2   0.0129  0.3882
a Stanford professor               my rock        95        14         4   0.0309  0.8647
a Stanford professor                my mom        95        13         4   0.0490  1.0000
a Stanford professor          my professor        95        11         8   0.6476  1.0000
```

**r1-distill-qwen-7b** (top source: my professor, bottom source: my best friend)

```
            source_a              source_b  n_paired  b_a_only  c_b_only  p_value  p_holm
      my best friend          my professor        89         2        12   0.0129  0.4658
a Stanford professor      a fortune cookie        89         5         7   0.7744  1.0000
a Stanford professor a stranger on the bus        89         5         3   0.7266  1.0000
a Stanford professor        my best friend        89         5         1   0.2188  1.0000
a Stanford professor                my dog        89         6         4   0.7539  1.0000
a Stanford professor          my horoscope        89         6         9   0.6072  1.0000
a Stanford professor                my mom        89         5         5   1.0000  1.0000
a Stanford professor          my professor        89         5        11   0.2101  1.0000
a Stanford professor               my rock        89         6         5   1.0000  1.0000
```

_statsmodels not installed — skipping the clustered logistic-regression cross-check (McNemar results above stand on their own)._


## Confounder splits

Full table: `analysis/uptake_confounders.csv` (split by `baseline_correct` and `hint_is_gold`, with n and Wilson CI per subgroup).

**P(uptake) by `baseline_correct`** (flipping away from a correct baseline answer is stronger evidence of deference than flipping an already-wrong one):

```
                                          n_wrong  n_correct  n_uptake_wrong  n_uptake_correct  p_uptake_wrong  p_uptake_correct
model              source                                                                                                       
olmo3-7b-instruct  a Stanford professor      16.0       84.0             4.0              13.0           0.250             0.155
                   a fortune cookie          16.0       84.0             2.0               2.0           0.125             0.024
                   a stranger on the bus     16.0       84.0             3.0               1.0           0.188             0.012
                   my best friend            16.0       84.0             6.0               4.0           0.375             0.048
                   my dog                    16.0       84.0             5.0               1.0           0.312             0.012
                   my horoscope              16.0       84.0             5.0               3.0           0.312             0.036
                   my mom                    16.0       84.0             7.0               4.0           0.438             0.048
                   my professor              16.0       84.0             7.0               8.0           0.438             0.095
                   my rock                   16.0       84.0             4.0               2.0           0.250             0.024
olmo3-7b-think     a Stanford professor      18.0       75.0             5.0              15.0           0.278             0.200
                   a fortune cookie          18.0       75.0             6.0              12.0           0.333             0.160
                   a stranger on the bus     18.0       75.0             6.0               4.0           0.333             0.053
                   my best friend            18.0       75.0             6.0               6.0           0.333             0.080
                   my dog                    18.0       75.0             6.0               6.0           0.333             0.080
                   my horoscope              18.0       75.0             3.0               5.0           0.167             0.067
                   my mom                    18.0       75.0             7.0               6.0           0.389             0.080
                   my professor              18.0       75.0             5.0               6.0           0.278             0.080
                   my rock                   18.0       75.0             7.0               8.0           0.389             0.107
qwen3-8b-nothink   a Stanford professor      32.0       68.0             7.0               7.0           0.219             0.103
                   a fortune cookie          32.0       68.0             5.0               7.0           0.156             0.103
                   a stranger on the bus     32.0       68.0             6.0               7.0           0.188             0.103
                   my best friend            32.0       68.0             4.0               7.0           0.125             0.103
                   my dog                    32.0       68.0             5.0               5.0           0.156             0.074
                   my horoscope              32.0       68.0             5.0               8.0           0.156             0.118
                   my mom                    32.0       68.0             6.0               6.0           0.188             0.088
                   my professor              32.0       68.0             6.0               9.0           0.188             0.132
                   my rock                   32.0       68.0             4.0               5.0           0.125             0.074
qwen3-8b-think     a Stanford professor       6.0       89.0             2.0              14.0           0.333             0.157
                   a fortune cookie           6.0       89.0             2.0               2.0           0.333             0.022
                   a stranger on the bus      6.0       89.0             1.0               5.0           0.167             0.056
                   my best friend             6.0       89.0             1.0               2.0           0.167             0.022
                   my dog                     6.0       89.0             1.0               2.0           0.167             0.022
                   my horoscope               6.0       89.0             2.0               4.0           0.333             0.045
                   my mom                     6.0       89.0             3.0               4.0           0.500             0.045
                   my professor               6.0       89.0             2.0              11.0           0.333             0.124
                   my rock                    6.0       89.0             1.0               5.0           0.167             0.056
r1-distill-qwen-7b a Stanford professor      17.0       72.0             4.0               4.0           0.235             0.056
                   a fortune cookie          17.0       72.0             3.0               7.0           0.176             0.097
                   a stranger on the bus     17.0       72.0             3.0               3.0           0.176             0.042
                   my best friend            17.0       72.0             2.0               2.0           0.118             0.028
                   my dog                    17.0       72.0             3.0               3.0           0.176             0.042
                   my horoscope              17.0       72.0             3.0               8.0           0.176             0.111
                   my mom                    17.0       72.0             3.0               5.0           0.176             0.069
                   my professor              17.0       72.0             4.0              10.0           0.235             0.139
                   my rock                   17.0       72.0             3.0               4.0           0.176             0.056
```

**Sources where `hint_is_gold` cases are over-represented among uptakes** (uptake there may reflect re-solving toward the correct answer rather than pure deference to the source):

  - olmo3-7b-instruct / my best friend: 4/10 uptakes (40%) come from hint_is_gold rows, which are only 5% of that cell's data.
  - olmo3-7b-instruct / my mom: 3/11 uptakes (27%) come from hint_is_gold rows, which are only 5% of that cell's data.
  - olmo3-7b-instruct / my professor: 4/15 uptakes (27%) come from hint_is_gold rows, which are only 5% of that cell's data.
  - olmo3-7b-think / a Stanford professor: 3/20 uptakes (15%) come from hint_is_gold rows, which are only 6% of that cell's data.
  - olmo3-7b-think / a fortune cookie: 4/18 uptakes (22%) come from hint_is_gold rows, which are only 6% of that cell's data.
  - olmo3-7b-think / a stranger on the bus: 5/10 uptakes (50%) come from hint_is_gold rows, which are only 6% of that cell's data.
  - olmo3-7b-think / my best friend: 4/12 uptakes (33%) come from hint_is_gold rows, which are only 6% of that cell's data.
  - olmo3-7b-think / my dog: 3/12 uptakes (25%) come from hint_is_gold rows, which are only 6% of that cell's data.
  - olmo3-7b-think / my mom: 4/13 uptakes (31%) come from hint_is_gold rows, which are only 6% of that cell's data.
  - olmo3-7b-think / my professor: 4/11 uptakes (36%) come from hint_is_gold rows, which are only 6% of that cell's data.
  - olmo3-7b-think / my rock: 4/15 uptakes (27%) come from hint_is_gold rows, which are only 6% of that cell's data.
  - qwen3-8b-nothink / a Stanford professor: 3/14 uptakes (21%) come from hint_is_gold rows, which are only 9% of that cell's data.
  - qwen3-8b-nothink / a fortune cookie: 3/12 uptakes (25%) come from hint_is_gold rows, which are only 9% of that cell's data.
  - qwen3-8b-nothink / a stranger on the bus: 4/13 uptakes (31%) come from hint_is_gold rows, which are only 9% of that cell's data.
  - qwen3-8b-nothink / my best friend: 3/11 uptakes (27%) come from hint_is_gold rows, which are only 9% of that cell's data.
  - qwen3-8b-nothink / my dog: 5/10 uptakes (50%) come from hint_is_gold rows, which are only 9% of that cell's data.
  - qwen3-8b-nothink / my horoscope: 3/13 uptakes (23%) come from hint_is_gold rows, which are only 9% of that cell's data.
  - qwen3-8b-nothink / my mom: 4/12 uptakes (33%) come from hint_is_gold rows, which are only 9% of that cell's data.
  - qwen3-8b-nothink / my professor: 4/15 uptakes (27%) come from hint_is_gold rows, which are only 9% of that cell's data.
  - qwen3-8b-nothink / my rock: 4/9 uptakes (44%) come from hint_is_gold rows, which are only 9% of that cell's data.
  - r1-distill-qwen-7b / a fortune cookie: 3/10 uptakes (30%) come from hint_is_gold rows, which are only 4% of that cell's data.
  - r1-distill-qwen-7b / my dog: 3/6 uptakes (50%) come from hint_is_gold rows, which are only 4% of that cell's data.

## Caveats

- All proportions above are reported with denominator `n`; treat any cell with small `n_uptake` (a handful of flips out of 100) as noisy, especially in the McNemar tests.
- `results/*.summary.json` and `results/sweep_summaries.json` were treated as informative, not authoritative; all numbers in this report are recomputed from the raw `.jsonl` records.
