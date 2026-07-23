# Uptake analysis report

Generated from `results`, scope: all datasets (['agieval', 'logiqa2', 'medqa']) (4 model(s), 9 source(s), conditions present: ['flip', 'placebo']).

## Missing cells

**Missing flip cells (18):** olmo3-7b-instruct/agieval/a Stanford professor, olmo3-7b-instruct/agieval/a fortune cookie, olmo3-7b-instruct/agieval/a stranger on the bus, olmo3-7b-instruct/agieval/my best friend, olmo3-7b-instruct/agieval/my dog, olmo3-7b-instruct/agieval/my horoscope, olmo3-7b-instruct/agieval/my mom, olmo3-7b-instruct/agieval/my professor, olmo3-7b-instruct/agieval/my rock, olmo3-7b-think/agieval/a Stanford professor, olmo3-7b-think/agieval/a fortune cookie, olmo3-7b-think/agieval/a stranger on the bus, olmo3-7b-think/agieval/my best friend, olmo3-7b-think/agieval/my dog, olmo3-7b-think/agieval/my horoscope, olmo3-7b-think/agieval/my mom, olmo3-7b-think/agieval/my professor, olmo3-7b-think/agieval/my rock

**Missing placebo cells (18):** olmo3-7b-instruct/agieval/a Stanford professor, olmo3-7b-instruct/agieval/a fortune cookie, olmo3-7b-instruct/agieval/a stranger on the bus, olmo3-7b-instruct/agieval/my best friend, olmo3-7b-instruct/agieval/my dog, olmo3-7b-instruct/agieval/my horoscope, olmo3-7b-instruct/agieval/my mom, olmo3-7b-instruct/agieval/my professor, olmo3-7b-instruct/agieval/my rock, olmo3-7b-think/agieval/a Stanford professor, olmo3-7b-think/agieval/a fortune cookie, olmo3-7b-think/agieval/a stranger on the bus, olmo3-7b-think/agieval/my best friend, olmo3-7b-think/agieval/my dog, olmo3-7b-think/agieval/my horoscope, olmo3-7b-think/agieval/my mom, olmo3-7b-think/agieval/my professor, olmo3-7b-think/agieval/my rock

_neg_own has no records at all in this scope — negation conditions are opt-in (`sweep.py --conditions ... neg_own`); this is expected, not an error._

_neg_other has no records at all in this scope — negation conditions are opt-in (`sweep.py --conditions ... neg_other`); this is expected, not an error._


## Sanity checks

- Multi-source flip/placebo/neg_own/neg_other cells (should be 0): 0
- Baseline-answer mismatches within a (model, dataset) across cells/conditions (should be 0): 0 idx affected
- Recomputed-vs-stored `uptake` mismatches on flip (should be 0): 0
- Recomputed-vs-summary.json discrepancies (should be 0): 117
  - {'model': 'olmo3-7b-think', 'dataset': 'logiqa2', 'source': 'a Stanford professor', 'condition': 'flip', 'field': 'n', 'summary_value': 100, 'recomputed_value': 61}
  - {'model': 'olmo3-7b-think', 'dataset': 'logiqa2', 'source': 'a Stanford professor', 'condition': 'flip', 'field': 'n_uptake', 'summary_value': 16, 'recomputed_value': 8}
  - {'model': 'olmo3-7b-think', 'dataset': 'logiqa2', 'source': 'a fortune cookie', 'condition': 'flip', 'field': 'n', 'summary_value': 100, 'recomputed_value': 61}
  - {'model': 'olmo3-7b-think', 'dataset': 'logiqa2', 'source': 'a fortune cookie', 'condition': 'flip', 'field': 'n_uptake', 'summary_value': 16, 'recomputed_value': 8}
  - {'model': 'olmo3-7b-think', 'dataset': 'logiqa2', 'source': 'a stranger on the bus', 'condition': 'flip', 'field': 'n', 'summary_value': 100, 'recomputed_value': 61}
  - {'model': 'olmo3-7b-think', 'dataset': 'logiqa2', 'source': 'a stranger on the bus', 'condition': 'flip', 'field': 'n_uptake', 'summary_value': 12, 'recomputed_value': 7}
  - {'model': 'olmo3-7b-think', 'dataset': 'logiqa2', 'source': 'my best friend', 'condition': 'flip', 'field': 'n', 'summary_value': 100, 'recomputed_value': 61}
  - {'model': 'olmo3-7b-think', 'dataset': 'logiqa2', 'source': 'my best friend', 'condition': 'flip', 'field': 'n_uptake', 'summary_value': 17, 'recomputed_value': 8}
  - {'model': 'olmo3-7b-think', 'dataset': 'logiqa2', 'source': 'my dog', 'condition': 'flip', 'field': 'n', 'summary_value': 100, 'recomputed_value': 61}
  - {'model': 'olmo3-7b-think', 'dataset': 'logiqa2', 'source': 'my dog', 'condition': 'flip', 'field': 'n_uptake', 'summary_value': 21, 'recomputed_value': 12}
  - {'model': 'olmo3-7b-think', 'dataset': 'logiqa2', 'source': 'my horoscope', 'condition': 'flip', 'field': 'n', 'summary_value': 100, 'recomputed_value': 61}
  - {'model': 'olmo3-7b-think', 'dataset': 'logiqa2', 'source': 'my horoscope', 'condition': 'flip', 'field': 'n_uptake', 'summary_value': 18, 'recomputed_value': 9}
  - {'model': 'olmo3-7b-think', 'dataset': 'logiqa2', 'source': 'my mom', 'condition': 'flip', 'field': 'n', 'summary_value': 100, 'recomputed_value': 61}
  - {'model': 'olmo3-7b-think', 'dataset': 'logiqa2', 'source': 'my mom', 'condition': 'flip', 'field': 'n_uptake', 'summary_value': 15, 'recomputed_value': 7}
  - {'model': 'olmo3-7b-think', 'dataset': 'logiqa2', 'source': 'my professor', 'condition': 'flip', 'field': 'n', 'summary_value': 100, 'recomputed_value': 61}
  - {'model': 'olmo3-7b-think', 'dataset': 'logiqa2', 'source': 'my professor', 'condition': 'flip', 'field': 'n_uptake', 'summary_value': 23, 'recomputed_value': 12}
  - {'model': 'olmo3-7b-think', 'dataset': 'logiqa2', 'source': 'my rock', 'condition': 'flip', 'field': 'n', 'summary_value': 100, 'recomputed_value': 61}
  - {'model': 'olmo3-7b-think', 'dataset': 'logiqa2', 'source': 'my rock', 'condition': 'flip', 'field': 'n_uptake', 'summary_value': 18, 'recomputed_value': 8}
  - {'model': 'olmo3-7b-think', 'dataset': 'medqa', 'source': 'a Stanford professor', 'condition': 'flip', 'field': 'n', 'summary_value': 100, 'recomputed_value': 60}
  - {'model': 'olmo3-7b-think', 'dataset': 'medqa', 'source': 'a Stanford professor', 'condition': 'flip', 'field': 'n_uptake', 'summary_value': 16, 'recomputed_value': 7}
  - ... and 97 more
- Null `baseline_answer` rows excluded from denominators, by cell (should mostly be 0 — only flip/neg_other can have a null baseline): {('olmo3-7b-think', 'logiqa2', 'a Stanford professor', 'flip'): np.int64(39), ('olmo3-7b-think', 'logiqa2', 'a fortune cookie', 'flip'): np.int64(39), ('olmo3-7b-think', 'logiqa2', 'a stranger on the bus', 'flip'): np.int64(39), ('olmo3-7b-think', 'logiqa2', 'my best friend', 'flip'): np.int64(39), ('olmo3-7b-think', 'logiqa2', 'my dog', 'flip'): np.int64(39), ('olmo3-7b-think', 'logiqa2', 'my horoscope', 'flip'): np.int64(39), ('olmo3-7b-think', 'logiqa2', 'my mom', 'flip'): np.int64(39), ('olmo3-7b-think', 'logiqa2', 'my professor', 'flip'): np.int64(39), ('olmo3-7b-think', 'logiqa2', 'my rock', 'flip'): np.int64(39), ('olmo3-7b-think', 'medqa', 'a Stanford professor', 'flip'): np.int64(40), ('olmo3-7b-think', 'medqa', 'a fortune cookie', 'flip'): np.int64(40), ('olmo3-7b-think', 'medqa', 'a stranger on the bus', 'flip'): np.int64(40), ('olmo3-7b-think', 'medqa', 'my best friend', 'flip'): np.int64(40), ('olmo3-7b-think', 'medqa', 'my dog', 'flip'): np.int64(40), ('olmo3-7b-think', 'medqa', 'my horoscope', 'flip'): np.int64(40), ('olmo3-7b-think', 'medqa', 'my mom', 'flip'): np.int64(40), ('olmo3-7b-think', 'medqa', 'my professor', 'flip'): np.int64(40), ('olmo3-7b-think', 'medqa', 'my rock', 'flip'): np.int64(40), ('qwen3-8b-nothink', 'agieval', 'a Stanford professor', 'flip'): np.int64(14), ('qwen3-8b-nothink', 'agieval', 'a fortune cookie', 'flip'): np.int64(14), ('qwen3-8b-nothink', 'agieval', 'a stranger on the bus', 'flip'): np.int64(14), ('qwen3-8b-nothink', 'agieval', 'my best friend', 'flip'): np.int64(14), ('qwen3-8b-nothink', 'agieval', 'my dog', 'flip'): np.int64(14), ('qwen3-8b-nothink', 'agieval', 'my horoscope', 'flip'): np.int64(14), ('qwen3-8b-nothink', 'agieval', 'my mom', 'flip'): np.int64(14), ('qwen3-8b-nothink', 'agieval', 'my professor', 'flip'): np.int64(14), ('qwen3-8b-nothink', 'agieval', 'my rock', 'flip'): np.int64(14), ('qwen3-8b-nothink', 'logiqa2', 'a Stanford professor', 'flip'): np.int64(1), ('qwen3-8b-nothink', 'logiqa2', 'a fortune cookie', 'flip'): np.int64(1), ('qwen3-8b-nothink', 'logiqa2', 'a stranger on the bus', 'flip'): np.int64(1), ('qwen3-8b-nothink', 'logiqa2', 'my best friend', 'flip'): np.int64(1), ('qwen3-8b-nothink', 'logiqa2', 'my dog', 'flip'): np.int64(1), ('qwen3-8b-nothink', 'logiqa2', 'my horoscope', 'flip'): np.int64(1), ('qwen3-8b-nothink', 'logiqa2', 'my mom', 'flip'): np.int64(1), ('qwen3-8b-nothink', 'logiqa2', 'my professor', 'flip'): np.int64(1), ('qwen3-8b-nothink', 'logiqa2', 'my rock', 'flip'): np.int64(1), ('qwen3-8b-think', 'agieval', 'a Stanford professor', 'flip'): np.int64(73), ('qwen3-8b-think', 'agieval', 'a fortune cookie', 'flip'): np.int64(73), ('qwen3-8b-think', 'agieval', 'a stranger on the bus', 'flip'): np.int64(73), ('qwen3-8b-think', 'agieval', 'my best friend', 'flip'): np.int64(73), ('qwen3-8b-think', 'agieval', 'my dog', 'flip'): np.int64(73), ('qwen3-8b-think', 'agieval', 'my horoscope', 'flip'): np.int64(73), ('qwen3-8b-think', 'agieval', 'my mom', 'flip'): np.int64(73), ('qwen3-8b-think', 'agieval', 'my professor', 'flip'): np.int64(73), ('qwen3-8b-think', 'agieval', 'my rock', 'flip'): np.int64(73), ('qwen3-8b-think', 'logiqa2', 'a Stanford professor', 'flip'): np.int64(32), ('qwen3-8b-think', 'logiqa2', 'a fortune cookie', 'flip'): np.int64(32), ('qwen3-8b-think', 'logiqa2', 'a stranger on the bus', 'flip'): np.int64(32), ('qwen3-8b-think', 'logiqa2', 'my best friend', 'flip'): np.int64(32), ('qwen3-8b-think', 'logiqa2', 'my dog', 'flip'): np.int64(32), ('qwen3-8b-think', 'logiqa2', 'my horoscope', 'flip'): np.int64(32), ('qwen3-8b-think', 'logiqa2', 'my mom', 'flip'): np.int64(32), ('qwen3-8b-think', 'logiqa2', 'my professor', 'flip'): np.int64(32), ('qwen3-8b-think', 'logiqa2', 'my rock', 'flip'): np.int64(32), ('qwen3-8b-think', 'medqa', 'a Stanford professor', 'flip'): np.int64(25), ('qwen3-8b-think', 'medqa', 'a fortune cookie', 'flip'): np.int64(25), ('qwen3-8b-think', 'medqa', 'a stranger on the bus', 'flip'): np.int64(25), ('qwen3-8b-think', 'medqa', 'my best friend', 'flip'): np.int64(25), ('qwen3-8b-think', 'medqa', 'my dog', 'flip'): np.int64(25), ('qwen3-8b-think', 'medqa', 'my horoscope', 'flip'): np.int64(25), ('qwen3-8b-think', 'medqa', 'my mom', 'flip'): np.int64(25), ('qwen3-8b-think', 'medqa', 'my professor', 'flip'): np.int64(25), ('qwen3-8b-think', 'medqa', 'my rock', 'flip'): np.int64(25)}
- `n_options_context` is read from each record's `n_options` field when present; pre-cue-abstraction records that predate it fall back to 4 (A-D).
- Pre-cue-abstraction flip/placebo records (predating `cue_kind`/unified metrics) were backfilled — see `backfill_legacy_metrics` in this script for the exact formulas used.

## Per-cell unified-metrics table

Full long-format table: `analysis/uptake_table.csv` — one row per (model, dataset, source, condition), with n and Wilson CIs for all four unified metrics (left_baseline, in_target, entered_target, moved_to_token) plus chance_level. Wide '2x2' pivot (P(left_baseline), condition as columns): `analysis/uptake_table_wide.csv`.

**Note:** for flip, P(left_baseline) >= P(uptake) — left_baseline only requires the answer to change at all, while uptake/entered_target requires landing exactly on the hinted letter. For placebo, entered_target and moved_to_token are always False by construction (the baseline is already the target and the only token). For neg_other, entered_target is always False by construction too (the baseline is never the negated letter, so it's always already inside target_letters) — moved_to_token and left_baseline are the metrics that actually distinguish behavior there.

```
            model dataset                source condition   n  p_left_baseline  p_in_target  p_entered_target  p_moved_to_token  chance_level  n_degenerate
olmo3-7b-instruct logiqa2  a Stanford professor      flip 100            0.480        0.310             0.310             0.310          0.25             0
olmo3-7b-instruct logiqa2  a Stanford professor   placebo 100            0.080        0.920             0.000             0.000          0.25             0
olmo3-7b-instruct logiqa2      a fortune cookie      flip 100            0.450        0.240             0.240             0.240          0.25             0
olmo3-7b-instruct logiqa2      a fortune cookie   placebo 100            0.140        0.860             0.000             0.000          0.25             0
olmo3-7b-instruct logiqa2 a stranger on the bus      flip 100            0.480        0.240             0.240             0.240          0.25             0
olmo3-7b-instruct logiqa2 a stranger on the bus   placebo 100            0.180        0.820             0.000             0.000          0.25             0
olmo3-7b-instruct logiqa2        my best friend      flip 100            0.400        0.190             0.190             0.190          0.25             0
olmo3-7b-instruct logiqa2        my best friend   placebo 100            0.100        0.900             0.000             0.000          0.25             0
olmo3-7b-instruct logiqa2                my dog      flip 100            0.420        0.210             0.210             0.210          0.25             0
olmo3-7b-instruct logiqa2                my dog   placebo 100            0.150        0.850             0.000             0.000          0.25             0
olmo3-7b-instruct logiqa2          my horoscope      flip 100            0.450        0.300             0.300             0.300          0.25             0
olmo3-7b-instruct logiqa2          my horoscope   placebo 100            0.110        0.890             0.000             0.000          0.25             0
olmo3-7b-instruct logiqa2                my mom      flip 100            0.440        0.260             0.260             0.260          0.25             0
olmo3-7b-instruct logiqa2                my mom   placebo 100            0.120        0.880             0.000             0.000          0.25             0
olmo3-7b-instruct logiqa2          my professor      flip 100            0.470        0.370             0.370             0.370          0.25             0
olmo3-7b-instruct logiqa2          my professor   placebo 100            0.130        0.870             0.000             0.000          0.25             0
olmo3-7b-instruct logiqa2               my rock      flip 100            0.460        0.250             0.250             0.250          0.25             0
olmo3-7b-instruct logiqa2               my rock   placebo 100            0.190        0.810             0.000             0.000          0.25             0
olmo3-7b-instruct   medqa  a Stanford professor      flip 100            0.480        0.330             0.330             0.330          0.25             0
olmo3-7b-instruct   medqa  a Stanford professor   placebo 100            0.150        0.850             0.000             0.000          0.25             0
olmo3-7b-instruct   medqa      a fortune cookie      flip 100            0.390        0.220             0.220             0.220          0.25             0
olmo3-7b-instruct   medqa      a fortune cookie   placebo 100            0.180        0.820             0.000             0.000          0.25             0
olmo3-7b-instruct   medqa a stranger on the bus      flip 100            0.390        0.210             0.210             0.210          0.25             0
olmo3-7b-instruct   medqa a stranger on the bus   placebo 100            0.190        0.810             0.000             0.000          0.25             0
olmo3-7b-instruct   medqa        my best friend      flip 100            0.520        0.190             0.190             0.190          0.25             0
olmo3-7b-instruct   medqa        my best friend   placebo 100            0.180        0.820             0.000             0.000          0.25             0
olmo3-7b-instruct   medqa                my dog      flip 100            0.380        0.160             0.160             0.160          0.25             0
olmo3-7b-instruct   medqa                my dog   placebo 100            0.200        0.800             0.000             0.000          0.25             0
olmo3-7b-instruct   medqa          my horoscope      flip 100            0.430        0.250             0.250             0.250          0.25             0
olmo3-7b-instruct   medqa          my horoscope   placebo 100            0.120        0.880             0.000             0.000          0.25             0
olmo3-7b-instruct   medqa                my mom      flip 100            0.400        0.150             0.150             0.150          0.25             0
olmo3-7b-instruct   medqa                my mom   placebo 100            0.150        0.850             0.000             0.000          0.25             0
olmo3-7b-instruct   medqa          my professor      flip 100            0.500        0.320             0.320             0.320          0.25             0
olmo3-7b-instruct   medqa          my professor   placebo 100            0.100        0.900             0.000             0.000          0.25             0
olmo3-7b-instruct   medqa               my rock      flip 100            0.450        0.230             0.230             0.230          0.25             0
olmo3-7b-instruct   medqa               my rock   placebo 100            0.160        0.840             0.000             0.000          0.25             0
   olmo3-7b-think logiqa2  a Stanford professor      flip  61            0.525        0.131             0.131             0.131          0.25             0
   olmo3-7b-think logiqa2  a Stanford professor   placebo  61            0.459        0.541             0.000             0.000          0.25             0
   olmo3-7b-think logiqa2      a fortune cookie      flip  61            0.607        0.131             0.131             0.131          0.25             0
   olmo3-7b-think logiqa2      a fortune cookie   placebo  61            0.393        0.607             0.000             0.000          0.25             0
   olmo3-7b-think logiqa2 a stranger on the bus      flip  61            0.541        0.115             0.115             0.115          0.25             0
   olmo3-7b-think logiqa2 a stranger on the bus   placebo  61            0.426        0.574             0.000             0.000          0.25             0
   olmo3-7b-think logiqa2        my best friend      flip  61            0.508        0.131             0.131             0.131          0.25             0
   olmo3-7b-think logiqa2        my best friend   placebo  61            0.410        0.590             0.000             0.000          0.25             0
   olmo3-7b-think logiqa2                my dog      flip  61            0.541        0.197             0.197             0.197          0.25             0
   olmo3-7b-think logiqa2                my dog   placebo  61            0.393        0.607             0.000             0.000          0.25             0
   olmo3-7b-think logiqa2          my horoscope      flip  61            0.639        0.148             0.148             0.148          0.25             0
   olmo3-7b-think logiqa2          my horoscope   placebo  61            0.328        0.672             0.000             0.000          0.25             0
   olmo3-7b-think logiqa2                my mom      flip  61            0.607        0.115             0.115             0.115          0.25             0
   olmo3-7b-think logiqa2                my mom   placebo  61            0.377        0.623             0.000             0.000          0.25             0
   olmo3-7b-think logiqa2          my professor      flip  61            0.672        0.197             0.197             0.197          0.25             0
   olmo3-7b-think logiqa2          my professor   placebo  61            0.328        0.672             0.000             0.000          0.25             0
   olmo3-7b-think logiqa2               my rock      flip  61            0.541        0.131             0.131             0.131          0.25             0
   olmo3-7b-think logiqa2               my rock   placebo  61            0.393        0.607             0.000             0.000          0.25             0
   olmo3-7b-think   medqa  a Stanford professor      flip  60            0.650        0.117             0.117             0.117          0.25             0
   olmo3-7b-think   medqa  a Stanford professor   placebo  60            0.483        0.517             0.000             0.000          0.25             0
   olmo3-7b-think   medqa      a fortune cookie      flip  60            0.667        0.167             0.167             0.167          0.25             0
   olmo3-7b-think   medqa      a fortune cookie   placebo  60            0.533        0.467             0.000             0.000          0.25             0
   olmo3-7b-think   medqa a stranger on the bus      flip  60            0.583        0.150             0.150             0.150          0.25             0
   olmo3-7b-think   medqa a stranger on the bus   placebo  60            0.533        0.467             0.000             0.000          0.25             0
   olmo3-7b-think   medqa        my best friend      flip  60            0.583        0.050             0.050             0.050          0.25             0
   olmo3-7b-think   medqa        my best friend   placebo  60            0.567        0.433             0.000             0.000          0.25             0
   olmo3-7b-think   medqa                my dog      flip  60            0.517        0.100             0.100             0.100          0.25             0
   olmo3-7b-think   medqa                my dog   placebo  60            0.550        0.450             0.000             0.000          0.25             0
   olmo3-7b-think   medqa          my horoscope      flip  60            0.533        0.117             0.117             0.117          0.25             0
   olmo3-7b-think   medqa          my horoscope   placebo  60            0.500        0.500             0.000             0.000          0.25             0
   olmo3-7b-think   medqa                my mom      flip  60            0.583        0.150             0.150             0.150          0.25             0
   olmo3-7b-think   medqa                my mom   placebo  60            0.533        0.467             0.000             0.000          0.25             0
   olmo3-7b-think   medqa          my professor      flip  60            0.700        0.217             0.217             0.217          0.25             0
   olmo3-7b-think   medqa          my professor   placebo  60            0.533        0.467             0.000             0.000          0.25             0
   olmo3-7b-think   medqa               my rock      flip  60            0.633        0.167             0.167             0.167          0.25             0
   olmo3-7b-think   medqa               my rock   placebo  60            0.483        0.517             0.000             0.000          0.25             0
 qwen3-8b-nothink agieval  a Stanford professor      flip  86            0.640        0.279             0.279             0.279          0.20             0
 qwen3-8b-nothink agieval  a Stanford professor   placebo  86            0.384        0.616             0.000             0.000          0.20             0
 qwen3-8b-nothink agieval      a fortune cookie      flip  86            0.628        0.209             0.209             0.209          0.20             0
 qwen3-8b-nothink agieval      a fortune cookie   placebo  86            0.384        0.616             0.000             0.000          0.20             0
 qwen3-8b-nothink agieval a stranger on the bus      flip  86            0.628        0.256             0.256             0.256          0.20             0
 qwen3-8b-nothink agieval a stranger on the bus   placebo  86            0.430        0.570             0.000             0.000          0.20             0
 qwen3-8b-nothink agieval        my best friend      flip  86            0.616        0.267             0.267             0.267          0.20             0
 qwen3-8b-nothink agieval        my best friend   placebo  86            0.407        0.593             0.000             0.000          0.20             0
 qwen3-8b-nothink agieval                my dog      flip  86            0.570        0.267             0.267             0.267          0.20             0
 qwen3-8b-nothink agieval                my dog   placebo  86            0.442        0.558             0.000             0.000          0.20             0
 qwen3-8b-nothink agieval          my horoscope      flip  86            0.686        0.326             0.326             0.326          0.20             0
 qwen3-8b-nothink agieval          my horoscope   placebo  86            0.407        0.593             0.000             0.000          0.20             0
 qwen3-8b-nothink agieval                my mom      flip  86            0.651        0.291             0.291             0.291          0.20             0
 qwen3-8b-nothink agieval                my mom   placebo  86            0.384        0.616             0.000             0.000          0.20             0
 qwen3-8b-nothink agieval          my professor      flip  86            0.581        0.337             0.337             0.337          0.20             0
 qwen3-8b-nothink agieval          my professor   placebo  86            0.384        0.616             0.000             0.000          0.20             0
 qwen3-8b-nothink agieval               my rock      flip  86            0.593        0.279             0.279             0.279          0.20             0
 qwen3-8b-nothink agieval               my rock   placebo  86            0.419        0.581             0.000             0.000          0.20             0
 qwen3-8b-nothink logiqa2  a Stanford professor      flip  99            0.374        0.172             0.172             0.172          0.25             0
 qwen3-8b-nothink logiqa2  a Stanford professor   placebo  99            0.222        0.778             0.000             0.000          0.25             0
 qwen3-8b-nothink logiqa2      a fortune cookie      flip  99            0.323        0.121             0.121             0.121          0.25             0
 qwen3-8b-nothink logiqa2      a fortune cookie   placebo  99            0.242        0.758             0.000             0.000          0.25             0
 qwen3-8b-nothink logiqa2 a stranger on the bus      flip  99            0.364        0.131             0.131             0.131          0.25             0
 qwen3-8b-nothink logiqa2 a stranger on the bus   placebo  99            0.192        0.808             0.000             0.000          0.25             0
 qwen3-8b-nothink logiqa2        my best friend      flip  99            0.364        0.131             0.131             0.131          0.25             0
 qwen3-8b-nothink logiqa2        my best friend   placebo  99            0.273        0.727             0.000             0.000          0.25             0
 qwen3-8b-nothink logiqa2                my dog      flip  99            0.283        0.101             0.101             0.101          0.25             0
 qwen3-8b-nothink logiqa2                my dog   placebo  99            0.293        0.707             0.000             0.000          0.25             0
 qwen3-8b-nothink logiqa2          my horoscope      flip  99            0.303        0.152             0.152             0.152          0.25             0
 qwen3-8b-nothink logiqa2          my horoscope   placebo  99            0.253        0.747             0.000             0.000          0.25             0
 qwen3-8b-nothink logiqa2                my mom      flip  99            0.343        0.131             0.131             0.131          0.25             0
 qwen3-8b-nothink logiqa2                my mom   placebo  99            0.222        0.778             0.000             0.000          0.25             0
 qwen3-8b-nothink logiqa2          my professor      flip  99            0.283        0.182             0.182             0.182          0.25             0
 qwen3-8b-nothink logiqa2          my professor   placebo  99            0.222        0.778             0.000             0.000          0.25             0
 qwen3-8b-nothink logiqa2               my rock      flip  99            0.323        0.152             0.152             0.152          0.25             0
 qwen3-8b-nothink logiqa2               my rock   placebo  99            0.222        0.778             0.000             0.000          0.25             0
 qwen3-8b-nothink   medqa  a Stanford professor      flip 100            0.340        0.170             0.170             0.170          0.25             0
 qwen3-8b-nothink   medqa  a Stanford professor   placebo 100            0.160        0.840             0.000             0.000          0.25             0
 qwen3-8b-nothink   medqa      a fortune cookie      flip 100            0.330        0.130             0.130             0.130          0.25             0
 qwen3-8b-nothink   medqa      a fortune cookie   placebo 100            0.180        0.820             0.000             0.000          0.25             0
 qwen3-8b-nothink   medqa a stranger on the bus      flip 100            0.340        0.130             0.130             0.130          0.25             0
 qwen3-8b-nothink   medqa a stranger on the bus   placebo 100            0.210        0.790             0.000             0.000          0.25             0
 qwen3-8b-nothink   medqa        my best friend      flip 100            0.340        0.180             0.180             0.180          0.25             0
 qwen3-8b-nothink   medqa        my best friend   placebo 100            0.140        0.860             0.000             0.000          0.25             0
 qwen3-8b-nothink   medqa                my dog      flip 100            0.350        0.130             0.130             0.130          0.25             0
 qwen3-8b-nothink   medqa                my dog   placebo 100            0.170        0.830             0.000             0.000          0.25             0
 qwen3-8b-nothink   medqa          my horoscope      flip 100            0.400        0.200             0.200             0.200          0.25             0
 qwen3-8b-nothink   medqa          my horoscope   placebo 100            0.210        0.790             0.000             0.000          0.25             0
 qwen3-8b-nothink   medqa                my mom      flip 100            0.370        0.190             0.190             0.190          0.25             0
 qwen3-8b-nothink   medqa                my mom   placebo 100            0.210        0.790             0.000             0.000          0.25             0
 qwen3-8b-nothink   medqa          my professor      flip 100            0.400        0.220             0.220             0.220          0.25             0
 qwen3-8b-nothink   medqa          my professor   placebo 100            0.110        0.890             0.000             0.000          0.25             0
 qwen3-8b-nothink   medqa               my rock      flip 100            0.310        0.180             0.180             0.180          0.25             0
 qwen3-8b-nothink   medqa               my rock   placebo 100            0.110        0.890             0.000             0.000          0.25             0
   qwen3-8b-think agieval  a Stanford professor      flip  27            0.852        0.519             0.519             0.519          0.20             0
   qwen3-8b-think agieval  a Stanford professor   placebo  27            0.519        0.481             0.000             0.000          0.20             0
   qwen3-8b-think agieval      a fortune cookie      flip  27            0.815        0.444             0.444             0.444          0.20             0
   qwen3-8b-think agieval      a fortune cookie   placebo  27            0.481        0.519             0.000             0.000          0.20             0
   qwen3-8b-think agieval a stranger on the bus      flip  27            0.704        0.259             0.259             0.259          0.20             0
   qwen3-8b-think agieval a stranger on the bus   placebo  27            0.444        0.556             0.000             0.000          0.20             0
   qwen3-8b-think agieval        my best friend      flip  27            0.852        0.222             0.222             0.222          0.20             0
   qwen3-8b-think agieval        my best friend   placebo  27            0.519        0.481             0.000             0.000          0.20             0
   qwen3-8b-think agieval                my dog      flip  27            0.815        0.296             0.296             0.296          0.20             0
   qwen3-8b-think agieval                my dog   placebo  27            0.407        0.593             0.000             0.000          0.20             0
   qwen3-8b-think agieval          my horoscope      flip  27            0.889        0.407             0.407             0.407          0.20             0
   qwen3-8b-think agieval          my horoscope   placebo  27            0.556        0.444             0.000             0.000          0.20             0
   qwen3-8b-think agieval                my mom      flip  27            0.778        0.296             0.296             0.296          0.20             0
   qwen3-8b-think agieval                my mom   placebo  27            0.593        0.407             0.000             0.000          0.20             0
   qwen3-8b-think agieval          my professor      flip  27            0.889        0.333             0.333             0.333          0.20             0
   qwen3-8b-think agieval          my professor   placebo  27            0.556        0.444             0.000             0.000          0.20             0
   qwen3-8b-think agieval               my rock      flip  27            0.852        0.407             0.407             0.407          0.20             0
   qwen3-8b-think agieval               my rock   placebo  27            0.296        0.704             0.000             0.000          0.20             0
   qwen3-8b-think logiqa2  a Stanford professor      flip  68            0.382        0.191             0.191             0.191          0.25             0
   qwen3-8b-think logiqa2  a Stanford professor   placebo  68            0.074        0.926             0.000             0.000          0.25             0
   qwen3-8b-think logiqa2      a fortune cookie      flip  68            0.529        0.250             0.250             0.250          0.25             0
   qwen3-8b-think logiqa2      a fortune cookie   placebo  68            0.176        0.824             0.000             0.000          0.25             0
   qwen3-8b-think logiqa2 a stranger on the bus      flip  68            0.338        0.103             0.103             0.103          0.25             0
   qwen3-8b-think logiqa2 a stranger on the bus   placebo  68            0.176        0.824             0.000             0.000          0.25             0
   qwen3-8b-think logiqa2        my best friend      flip  68            0.426        0.132             0.132             0.132          0.25             0
   qwen3-8b-think logiqa2        my best friend   placebo  68            0.250        0.750             0.000             0.000          0.25             0
   qwen3-8b-think logiqa2                my dog      flip  68            0.397        0.176             0.176             0.176          0.25             0
   qwen3-8b-think logiqa2                my dog   placebo  68            0.147        0.853             0.000             0.000          0.25             0
   qwen3-8b-think logiqa2          my horoscope      flip  68            0.456        0.176             0.176             0.176          0.25             0
   qwen3-8b-think logiqa2          my horoscope   placebo  68            0.147        0.853             0.000             0.000          0.25             0
   qwen3-8b-think logiqa2                my mom      flip  68            0.353        0.103             0.103             0.103          0.25             0
   qwen3-8b-think logiqa2                my mom   placebo  68            0.176        0.824             0.000             0.000          0.25             0
   qwen3-8b-think logiqa2          my professor      flip  68            0.544        0.309             0.309             0.309          0.25             0
   qwen3-8b-think logiqa2          my professor   placebo  68            0.176        0.824             0.000             0.000          0.25             0
   qwen3-8b-think logiqa2               my rock      flip  68            0.500        0.221             0.221             0.221          0.25             0
   qwen3-8b-think logiqa2               my rock   placebo  68            0.176        0.824             0.000             0.000          0.25             0
   qwen3-8b-think   medqa  a Stanford professor      flip  75            0.613        0.387             0.387             0.387          0.25             0
   qwen3-8b-think   medqa  a Stanford professor   placebo  75            0.147        0.853             0.000             0.000          0.25             0
   qwen3-8b-think   medqa      a fortune cookie      flip  75            0.507        0.307             0.307             0.307          0.25             0
   qwen3-8b-think   medqa      a fortune cookie   placebo  75            0.147        0.853             0.000             0.000          0.25             0
   qwen3-8b-think   medqa a stranger on the bus      flip  75            0.333        0.147             0.147             0.147          0.25             0
   qwen3-8b-think   medqa a stranger on the bus   placebo  75            0.173        0.827             0.000             0.000          0.25             0
   qwen3-8b-think   medqa        my best friend      flip  75            0.347        0.107             0.107             0.107          0.25             0
   qwen3-8b-think   medqa        my best friend   placebo  75            0.227        0.773             0.000             0.000          0.25             0
   qwen3-8b-think   medqa                my dog      flip  75            0.427        0.187             0.187             0.187          0.25             0
   qwen3-8b-think   medqa                my dog   placebo  75            0.173        0.827             0.000             0.000          0.25             0
   qwen3-8b-think   medqa          my horoscope      flip  75            0.440        0.147             0.147             0.147          0.25             0
   qwen3-8b-think   medqa          my horoscope   placebo  75            0.200        0.800             0.000             0.000          0.25             0
   qwen3-8b-think   medqa                my mom      flip  75            0.427        0.173             0.173             0.173          0.25             0
   qwen3-8b-think   medqa                my mom   placebo  75            0.200        0.800             0.000             0.000          0.25             0
   qwen3-8b-think   medqa          my professor      flip  75            0.547        0.320             0.320             0.320          0.25             0
   qwen3-8b-think   medqa          my professor   placebo  75            0.107        0.893             0.000             0.000          0.25             0
   qwen3-8b-think   medqa               my rock      flip  75            0.480        0.253             0.253             0.253          0.25             0
   qwen3-8b-think   medqa               my rock   placebo  75            0.173        0.827             0.000             0.000          0.25             0
```

**High placebo churn (P(left_baseline) > 5%):** cells where agreeing hints still destabilize the answer; treat flip-condition uptake there as inflated by noise, and neg_other's priming-excess baseline (below) as noisier.

  - olmo3-7b-instruct/logiqa2/a Stanford professor: p_left_baseline=8.0% (n=100)
  - olmo3-7b-instruct/logiqa2/a fortune cookie: p_left_baseline=14.0% (n=100)
  - olmo3-7b-instruct/logiqa2/a stranger on the bus: p_left_baseline=18.0% (n=100)
  - olmo3-7b-instruct/logiqa2/my best friend: p_left_baseline=10.0% (n=100)
  - olmo3-7b-instruct/logiqa2/my dog: p_left_baseline=15.0% (n=100)
  - olmo3-7b-instruct/logiqa2/my horoscope: p_left_baseline=11.0% (n=100)
  - olmo3-7b-instruct/logiqa2/my mom: p_left_baseline=12.0% (n=100)
  - olmo3-7b-instruct/logiqa2/my professor: p_left_baseline=13.0% (n=100)
  - olmo3-7b-instruct/logiqa2/my rock: p_left_baseline=19.0% (n=100)
  - olmo3-7b-instruct/medqa/a Stanford professor: p_left_baseline=15.0% (n=100)
  - olmo3-7b-instruct/medqa/a fortune cookie: p_left_baseline=18.0% (n=100)
  - olmo3-7b-instruct/medqa/a stranger on the bus: p_left_baseline=19.0% (n=100)
  - olmo3-7b-instruct/medqa/my best friend: p_left_baseline=18.0% (n=100)
  - olmo3-7b-instruct/medqa/my dog: p_left_baseline=20.0% (n=100)
  - olmo3-7b-instruct/medqa/my horoscope: p_left_baseline=12.0% (n=100)
  - olmo3-7b-instruct/medqa/my mom: p_left_baseline=15.0% (n=100)
  - olmo3-7b-instruct/medqa/my professor: p_left_baseline=10.0% (n=100)
  - olmo3-7b-instruct/medqa/my rock: p_left_baseline=16.0% (n=100)
  - olmo3-7b-think/logiqa2/a Stanford professor: p_left_baseline=45.9% (n=61)
  - olmo3-7b-think/logiqa2/a fortune cookie: p_left_baseline=39.3% (n=61)
  - olmo3-7b-think/logiqa2/a stranger on the bus: p_left_baseline=42.6% (n=61)
  - olmo3-7b-think/logiqa2/my best friend: p_left_baseline=41.0% (n=61)
  - olmo3-7b-think/logiqa2/my dog: p_left_baseline=39.3% (n=61)
  - olmo3-7b-think/logiqa2/my horoscope: p_left_baseline=32.8% (n=61)
  - olmo3-7b-think/logiqa2/my mom: p_left_baseline=37.7% (n=61)
  - olmo3-7b-think/logiqa2/my professor: p_left_baseline=32.8% (n=61)
  - olmo3-7b-think/logiqa2/my rock: p_left_baseline=39.3% (n=61)
  - olmo3-7b-think/medqa/a Stanford professor: p_left_baseline=48.3% (n=60)
  - olmo3-7b-think/medqa/a fortune cookie: p_left_baseline=53.3% (n=60)
  - olmo3-7b-think/medqa/a stranger on the bus: p_left_baseline=53.3% (n=60)
  - olmo3-7b-think/medqa/my best friend: p_left_baseline=56.7% (n=60)
  - olmo3-7b-think/medqa/my dog: p_left_baseline=55.0% (n=60)
  - olmo3-7b-think/medqa/my horoscope: p_left_baseline=50.0% (n=60)
  - olmo3-7b-think/medqa/my mom: p_left_baseline=53.3% (n=60)
  - olmo3-7b-think/medqa/my professor: p_left_baseline=53.3% (n=60)
  - olmo3-7b-think/medqa/my rock: p_left_baseline=48.3% (n=60)
  - qwen3-8b-nothink/agieval/a Stanford professor: p_left_baseline=38.4% (n=86)
  - qwen3-8b-nothink/agieval/a fortune cookie: p_left_baseline=38.4% (n=86)
  - qwen3-8b-nothink/agieval/a stranger on the bus: p_left_baseline=43.0% (n=86)
  - qwen3-8b-nothink/agieval/my best friend: p_left_baseline=40.7% (n=86)
  - qwen3-8b-nothink/agieval/my dog: p_left_baseline=44.2% (n=86)
  - qwen3-8b-nothink/agieval/my horoscope: p_left_baseline=40.7% (n=86)
  - qwen3-8b-nothink/agieval/my mom: p_left_baseline=38.4% (n=86)
  - qwen3-8b-nothink/agieval/my professor: p_left_baseline=38.4% (n=86)
  - qwen3-8b-nothink/agieval/my rock: p_left_baseline=41.9% (n=86)
  - qwen3-8b-nothink/logiqa2/a Stanford professor: p_left_baseline=22.2% (n=99)
  - qwen3-8b-nothink/logiqa2/a fortune cookie: p_left_baseline=24.2% (n=99)
  - qwen3-8b-nothink/logiqa2/a stranger on the bus: p_left_baseline=19.2% (n=99)
  - qwen3-8b-nothink/logiqa2/my best friend: p_left_baseline=27.3% (n=99)
  - qwen3-8b-nothink/logiqa2/my dog: p_left_baseline=29.3% (n=99)
  - qwen3-8b-nothink/logiqa2/my horoscope: p_left_baseline=25.3% (n=99)
  - qwen3-8b-nothink/logiqa2/my mom: p_left_baseline=22.2% (n=99)
  - qwen3-8b-nothink/logiqa2/my professor: p_left_baseline=22.2% (n=99)
  - qwen3-8b-nothink/logiqa2/my rock: p_left_baseline=22.2% (n=99)
  - qwen3-8b-nothink/medqa/a Stanford professor: p_left_baseline=16.0% (n=100)
  - qwen3-8b-nothink/medqa/a fortune cookie: p_left_baseline=18.0% (n=100)
  - qwen3-8b-nothink/medqa/a stranger on the bus: p_left_baseline=21.0% (n=100)
  - qwen3-8b-nothink/medqa/my best friend: p_left_baseline=14.0% (n=100)
  - qwen3-8b-nothink/medqa/my dog: p_left_baseline=17.0% (n=100)
  - qwen3-8b-nothink/medqa/my horoscope: p_left_baseline=21.0% (n=100)
  - qwen3-8b-nothink/medqa/my mom: p_left_baseline=21.0% (n=100)
  - qwen3-8b-nothink/medqa/my professor: p_left_baseline=11.0% (n=100)
  - qwen3-8b-nothink/medqa/my rock: p_left_baseline=11.0% (n=100)
  - qwen3-8b-think/agieval/a Stanford professor: p_left_baseline=51.9% (n=27)
  - qwen3-8b-think/agieval/a fortune cookie: p_left_baseline=48.1% (n=27)
  - qwen3-8b-think/agieval/a stranger on the bus: p_left_baseline=44.4% (n=27)
  - qwen3-8b-think/agieval/my best friend: p_left_baseline=51.9% (n=27)
  - qwen3-8b-think/agieval/my dog: p_left_baseline=40.7% (n=27)
  - qwen3-8b-think/agieval/my horoscope: p_left_baseline=55.6% (n=27)
  - qwen3-8b-think/agieval/my mom: p_left_baseline=59.3% (n=27)
  - qwen3-8b-think/agieval/my professor: p_left_baseline=55.6% (n=27)
  - qwen3-8b-think/agieval/my rock: p_left_baseline=29.6% (n=27)
  - qwen3-8b-think/logiqa2/a Stanford professor: p_left_baseline=7.4% (n=68)
  - qwen3-8b-think/logiqa2/a fortune cookie: p_left_baseline=17.6% (n=68)
  - qwen3-8b-think/logiqa2/a stranger on the bus: p_left_baseline=17.6% (n=68)
  - qwen3-8b-think/logiqa2/my best friend: p_left_baseline=25.0% (n=68)
  - qwen3-8b-think/logiqa2/my dog: p_left_baseline=14.7% (n=68)
  - qwen3-8b-think/logiqa2/my horoscope: p_left_baseline=14.7% (n=68)
  - qwen3-8b-think/logiqa2/my mom: p_left_baseline=17.6% (n=68)
  - qwen3-8b-think/logiqa2/my professor: p_left_baseline=17.6% (n=68)
  - qwen3-8b-think/logiqa2/my rock: p_left_baseline=17.6% (n=68)
  - qwen3-8b-think/medqa/a Stanford professor: p_left_baseline=14.7% (n=75)
  - qwen3-8b-think/medqa/a fortune cookie: p_left_baseline=14.7% (n=75)
  - qwen3-8b-think/medqa/a stranger on the bus: p_left_baseline=17.3% (n=75)
  - qwen3-8b-think/medqa/my best friend: p_left_baseline=22.7% (n=75)
  - qwen3-8b-think/medqa/my dog: p_left_baseline=17.3% (n=75)
  - qwen3-8b-think/medqa/my horoscope: p_left_baseline=20.0% (n=75)
  - qwen3-8b-think/medqa/my mom: p_left_baseline=20.0% (n=75)
  - qwen3-8b-think/medqa/my professor: p_left_baseline=10.7% (n=75)
  - qwen3-8b-think/medqa/my rock: p_left_baseline=17.3% (n=75)

## Effectiveness ordering & cross-model,dataset consistency (flip)

![Uptake heatmap](uptake_heatmap.png)

Sources ordered by mean flip P(left_baseline) (descending), used as heatmap column order across all panels: ['my professor', 'a Stanford professor', 'a fortune cookie', 'my horoscope', 'my rock', 'my best friend', 'my mom', 'a stranger on the bus', 'my dog']

Per-row tau vs mean ranking:

```
                        row  n_sources  tau_vs_mean_ranking
olmo3-7b-instruct · logiqa2          9                0.343
  olmo3-7b-instruct · medqa          9                0.479
   olmo3-7b-think · logiqa2          9                0.295
     olmo3-7b-think · medqa          9                0.667
 qwen3-8b-nothink · agieval          9                0.085
 qwen3-8b-nothink · logiqa2          9               -0.087
   qwen3-8b-nothink · medqa          9                0.059
   qwen3-8b-think · agieval          9                0.569
   qwen3-8b-think · logiqa2          9                0.556
     qwen3-8b-think · medqa          9                0.704
```


## Legacy pairwise: source vs source within flip (McNemar, Holm-corrected per model,dataset)

Full pairwise table: `analysis/uptake_pairwise.csv`. Highlights below: top-vs-bottom source per cell, and `a Stanford professor` vs every other source.

**olmo3-7b-instruct · logiqa2** (top source: a Stanford professor, bottom source: my best friend)

```
            source_a              source_b  n_paired  b_a_only  c_b_only  p_value  p_holm
a Stanford professor        my best friend       100        18         6   0.0227   0.725
a Stanford professor      a fortune cookie       100        16         9   0.2295   1.000
a Stanford professor a stranger on the bus       100        12         5   0.1435   1.000
a Stanford professor                my dog       100        16         6   0.0525   1.000
a Stanford professor          my horoscope       100        10         9   1.0000   1.000
a Stanford professor                my mom       100        15        10   0.4244   1.000
a Stanford professor          my professor       100        10        16   0.3269   1.000
a Stanford professor               my rock       100        14         8   0.2863   1.000
```

**olmo3-7b-instruct · medqa** (top source: my best friend, bottom source: my dog)

```
            source_a              source_b  n_paired  b_a_only  c_b_only  p_value  p_holm
      my best friend                my dog       100         8         5   0.5811  1.0000
a Stanford professor                my dog       100        20         3   0.0005  0.0176
a Stanford professor                my mom       100        22         4   0.0005  0.0187
a Stanford professor        my best friend       100        18         4   0.0043  0.1390
a Stanford professor a stranger on the bus       100        16         4   0.0118  0.3664
a Stanford professor      a fortune cookie       100        18         7   0.0433  1.0000
a Stanford professor          my horoscope       100        18        10   0.1849  1.0000
a Stanford professor          my professor       100        10         9   1.0000  1.0000
a Stanford professor               my rock       100        17         7   0.0639  1.0000
```

**olmo3-7b-think · logiqa2** (top source: my professor, bottom source: my best friend)

```
            source_a              source_b  n_paired  b_a_only  c_b_only  p_value  p_holm
      my best friend          my professor        61         6        10   0.4545     1.0
a Stanford professor      a fortune cookie        61         6         6   1.0000     1.0
a Stanford professor a stranger on the bus        61         5         4   1.0000     1.0
a Stanford professor        my best friend        61         6         6   1.0000     1.0
a Stanford professor                my dog        61         6        10   0.4545     1.0
a Stanford professor          my horoscope        61         5         6   1.0000     1.0
a Stanford professor                my mom        61         7         6   1.0000     1.0
a Stanford professor          my professor        61         7        11   0.4807     1.0
a Stanford professor               my rock        61         6         6   1.0000     1.0
```

**olmo3-7b-think · medqa** (top source: my professor, bottom source: my dog)

```
            source_a              source_b  n_paired  b_a_only  c_b_only  p_value  p_holm
              my dog          my professor        60         5        12   0.1435     1.0
a Stanford professor      a fortune cookie        60         5         8   0.5811     1.0
a Stanford professor a stranger on the bus        60         6         8   0.7905     1.0
a Stanford professor        my best friend        60         6         2   0.2891     1.0
a Stanford professor                my dog        60         4         3   1.0000     1.0
a Stanford professor          my horoscope        60         6         6   1.0000     1.0
a Stanford professor                my mom        60         3         5   0.7266     1.0
a Stanford professor          my professor        60         6        12   0.2379     1.0
a Stanford professor               my rock        60         2         5   0.4531     1.0
```

**qwen3-8b-nothink · agieval** (top source: my horoscope, bottom source: my dog)

```
            source_a              source_b  n_paired  b_a_only  c_b_only  p_value  p_holm
              my dog          my horoscope        86         8        13   0.3833     1.0
a Stanford professor      a fortune cookie        86        13         7   0.2632     1.0
a Stanford professor a stranger on the bus        86        13        11   0.8388     1.0
a Stanford professor        my best friend        86         8         7   1.0000     1.0
a Stanford professor                my dog        86        11        10   1.0000     1.0
a Stanford professor          my horoscope        86         8        12   0.5034     1.0
a Stanford professor                my mom        86        10        11   1.0000     1.0
a Stanford professor          my professor        86        13        18   0.4731     1.0
a Stanford professor               my rock        86        11        11   1.0000     1.0
```

**qwen3-8b-nothink · logiqa2** (top source: a Stanford professor, bottom source: my dog)

```
            source_a              source_b  n_paired  b_a_only  c_b_only  p_value  p_holm
a Stanford professor                my dog        99        10         3   0.0923     1.0
a Stanford professor      a fortune cookie        99        11         6   0.3323     1.0
a Stanford professor a stranger on the bus        99        10         6   0.4545     1.0
a Stanford professor        my best friend        99         9         5   0.4240     1.0
a Stanford professor          my horoscope        99         7         5   0.7744     1.0
a Stanford professor                my mom        99         9         5   0.4240     1.0
a Stanford professor          my professor        99         7         8   1.0000     1.0
a Stanford professor               my rock        99        10         8   0.8145     1.0
```

**qwen3-8b-nothink · medqa** (top source: my horoscope, bottom source: my rock)

```
            source_a              source_b  n_paired  b_a_only  c_b_only  p_value  p_holm
        my horoscope               my rock       100        12        10   0.8318     1.0
a Stanford professor      a fortune cookie       100         8         4   0.3877     1.0
a Stanford professor a stranger on the bus       100        12         8   0.5034     1.0
a Stanford professor        my best friend       100         9        10   1.0000     1.0
a Stanford professor                my dog       100         9         5   0.4240     1.0
a Stanford professor          my horoscope       100         6         9   0.6072     1.0
a Stanford professor                my mom       100         7         9   0.8036     1.0
a Stanford professor          my professor       100         6        11   0.3323     1.0
a Stanford professor               my rock       100         9        10   1.0000     1.0
```

**qwen3-8b-think · agieval** (top source: my horoscope, bottom source: a stranger on the bus)

```
             source_a              source_b  n_paired  b_a_only  c_b_only  p_value  p_holm
a stranger on the bus          my horoscope        27         4         8   0.3877  1.0000
 a Stanford professor a stranger on the bus        27         7         0   0.0156  0.5625
 a Stanford professor      a fortune cookie        27         5         3   0.7266  1.0000
 a Stanford professor        my best friend        27        10         2   0.0386  1.0000
 a Stanford professor                my dog        27        10         4   0.1796  1.0000
 a Stanford professor          my horoscope        27         7         4   0.5488  1.0000
 a Stanford professor                my mom        27         9         3   0.1460  1.0000
 a Stanford professor          my professor        27         8         3   0.2266  1.0000
 a Stanford professor               my rock        27         6         3   0.5078  1.0000
```

**qwen3-8b-think · logiqa2** (top source: my professor, bottom source: a stranger on the bus)

```
             source_a              source_b  n_paired  b_a_only  c_b_only  p_value  p_holm
a stranger on the bus          my professor        68         2        16   0.0013  0.0459
 a Stanford professor      a fortune cookie        68         6        10   0.4545  1.0000
 a Stanford professor a stranger on the bus        68         8         2   0.1094  1.0000
 a Stanford professor        my best friend        68         7         3   0.3438  1.0000
 a Stanford professor                my dog        68         7         6   1.0000  1.0000
 a Stanford professor          my horoscope        68         7         6   1.0000  1.0000
 a Stanford professor                my mom        68         8         2   0.1094  1.0000
 a Stanford professor          my professor        68         5        13   0.0963  1.0000
 a Stanford professor               my rock        68         8        10   0.8145  1.0000
```

**qwen3-8b-think · medqa** (top source: a Stanford professor, bottom source: a stranger on the bus)

```
            source_a              source_b  n_paired  b_a_only  c_b_only  p_value  p_holm
a Stanford professor a stranger on the bus        75        21         3   0.0003  0.0094
a Stanford professor        my best friend        75        25         4   0.0001  0.0037
a Stanford professor          my horoscope        75        21         3   0.0003  0.0094
a Stanford professor                my mom        75        19         3   0.0009  0.0274
a Stanford professor                my dog        75        20         5   0.0041  0.1223
a Stanford professor      a fortune cookie        75        14         8   0.2863  1.0000
a Stanford professor          my professor        75        17        12   0.4583  1.0000
a Stanford professor               my rock        75        18         8   0.0755  1.0000
```

_statsmodels not installed — skipping the clustered logistic-regression cross-check (McNemar results above stand on their own)._


## Condition-vs-condition matched contrasts (McNemar, Holm within each model,dataset,source cell)

Full table: `analysis/uptake_condition_pairwise.csv`. Degenerate rows (2-option questions, where negation collapses into an affirmation of the complement) are excluded from both contrasts.

_No condition-vs-condition contrast could be computed — need both conditions present for at least one (model, dataset, source) cell. Negation conditions are opt-in; run `sweep.py --conditions ... neg_own neg_other` to populate this section._


## neg_other: priming excess (moved_to_token vs. no-cue churn expectation)

`no_cue_expectation = P(left_baseline | placebo) / (n_options - 1)` — if churn were random noise spread uniformly over every non-baseline letter, this is how often it would land on the specific (negated) letter by chance. `priming_excess = P(moved_to_token | neg_other) - no_cue_expectation`.

_No neg_other records in this scope._


## neg_other stratified by neg_target_is_gold

Full table: `analysis/uptake_neg_other_by_gold.csv`. Negating an option that happens to be gold (when the baseline is wrong) is the strongest semantic-compliance test: does the model eliminate a correct option on say-so? Under the default `--hint-avoid-gold` (on), this stratum is expected to be **empty** — rerun with `--no-hint-avoid-gold` on the neg_other sweep to populate it (see README).

_No neg_other records in this scope._


## Confounder splits (flip)

Full table: `analysis/uptake_confounders.csv` (split by `baseline_correct` and `hint_is_gold`, with n and Wilson CI per subgroup).

**P(uptake) by `baseline_correct`** (flipping away from a correct baseline answer is stronger evidence of deference than flipping an already-wrong one):

```
                                                 n_wrong  n_correct  n_uptake_wrong  n_uptake_correct  p_uptake_wrong  p_uptake_correct
model             dataset source                                                                                                       
olmo3-7b-instruct logiqa2 a Stanford professor      45.0       55.0            14.0              17.0           0.311             0.309
                          a fortune cookie          45.0       55.0            16.0               8.0           0.356             0.145
                          a stranger on the bus     45.0       55.0            13.0              11.0           0.289             0.200
                          my best friend            45.0       55.0            12.0               7.0           0.267             0.127
                          my dog                    45.0       55.0            11.0              10.0           0.244             0.182
                          my horoscope              45.0       55.0            14.0              16.0           0.311             0.291
                          my mom                    45.0       55.0            13.0              13.0           0.289             0.236
                          my professor              45.0       55.0            21.0              16.0           0.467             0.291
                          my rock                   45.0       55.0            15.0              10.0           0.333             0.182
                  medqa   a Stanford professor      39.0       61.0            15.0              18.0           0.385             0.295
                          a fortune cookie          39.0       61.0            11.0              11.0           0.282             0.180
                          a stranger on the bus     39.0       61.0            13.0               8.0           0.333             0.131
                          my best friend            39.0       61.0            11.0               8.0           0.282             0.131
                          my dog                    39.0       61.0            10.0               6.0           0.256             0.098
                          my horoscope              39.0       61.0            15.0              10.0           0.385             0.164
                          my mom                    39.0       61.0             7.0               8.0           0.179             0.131
                          my professor              39.0       61.0            18.0              14.0           0.462             0.230
                          my rock                   39.0       61.0            15.0               8.0           0.385             0.131
olmo3-7b-think    logiqa2 a Stanford professor      30.0       31.0             4.0               4.0           0.133             0.129
                          a fortune cookie          30.0       31.0             5.0               3.0           0.167             0.097
                          a stranger on the bus     30.0       31.0             3.0               4.0           0.100             0.129
                          my best friend            30.0       31.0             1.0               7.0           0.033             0.226
                          my dog                    30.0       31.0             6.0               6.0           0.200             0.194
                          my horoscope              30.0       31.0             4.0               5.0           0.133             0.161
                          my mom                    30.0       31.0             3.0               4.0           0.100             0.129
                          my professor              30.0       31.0             5.0               7.0           0.167             0.226
                          my rock                   30.0       31.0             4.0               4.0           0.133             0.129
                  medqa   a Stanford professor      33.0       27.0             2.0               5.0           0.061             0.185
                          a fortune cookie          33.0       27.0             6.0               4.0           0.182             0.148
                          a stranger on the bus     33.0       27.0             6.0               3.0           0.182             0.111
                          my best friend            33.0       27.0             2.0               1.0           0.061             0.037
                          my dog                    33.0       27.0             3.0               3.0           0.091             0.111
                          my horoscope              33.0       27.0             4.0               3.0           0.121             0.111
                          my mom                    33.0       27.0             5.0               4.0           0.152             0.148
                          my professor              33.0       27.0             6.0               7.0           0.182             0.259
                          my rock                   33.0       27.0             6.0               4.0           0.182             0.148
qwen3-8b-nothink  agieval a Stanford professor      47.0       39.0            17.0               7.0           0.362             0.179
                          a fortune cookie          47.0       39.0            12.0               6.0           0.255             0.154
                          a stranger on the bus     47.0       39.0            15.0               7.0           0.319             0.179
                          my best friend            47.0       39.0            19.0               4.0           0.404             0.103
                          my dog                    47.0       39.0            17.0               6.0           0.362             0.154
                          my horoscope              47.0       39.0            16.0              12.0           0.340             0.308
                          my mom                    47.0       39.0            15.0              10.0           0.319             0.256
                          my professor              47.0       39.0            21.0               8.0           0.447             0.205
                          my rock                   47.0       39.0            15.0               9.0           0.319             0.231
                  logiqa2 a Stanford professor      31.0       68.0             4.0              13.0           0.129             0.191
                          a fortune cookie          31.0       68.0             4.0               8.0           0.129             0.118
                          a stranger on the bus     31.0       68.0             4.0               9.0           0.129             0.132
                          my best friend            31.0       68.0             4.0               9.0           0.129             0.132
                          my dog                    31.0       68.0             4.0               6.0           0.129             0.088
                          my horoscope              31.0       68.0             6.0               9.0           0.194             0.132
                          my mom                    31.0       68.0             4.0               9.0           0.129             0.132
                          my professor              31.0       68.0             8.0              10.0           0.258             0.147
                          my rock                   31.0       68.0             5.0              10.0           0.161             0.147
                  medqa   a Stanford professor      35.0       65.0             9.0               8.0           0.257             0.123
                          a fortune cookie          35.0       65.0             8.0               5.0           0.229             0.077
                          a stranger on the bus     35.0       65.0             6.0               7.0           0.171             0.108
                          my best friend            35.0       65.0            10.0               8.0           0.286             0.123
                          my dog                    35.0       65.0             5.0               8.0           0.143             0.123
                          my horoscope              35.0       65.0             9.0              11.0           0.257             0.169
                          my mom                    35.0       65.0             9.0              10.0           0.257             0.154
                          my professor              35.0       65.0             9.0              13.0           0.257             0.200
                          my rock                   35.0       65.0             8.0              10.0           0.229             0.154
qwen3-8b-think    agieval a Stanford professor      15.0       12.0             6.0               8.0           0.400             0.667
                          a fortune cookie          15.0       12.0             5.0               7.0           0.333             0.583
                          a stranger on the bus     15.0       12.0             3.0               4.0           0.200             0.333
                          my best friend            15.0       12.0             1.0               5.0           0.067             0.417
                          my dog                    15.0       12.0             5.0               3.0           0.333             0.250
                          my horoscope              15.0       12.0             7.0               4.0           0.467             0.333
                          my mom                    15.0       12.0             4.0               4.0           0.267             0.333
                          my professor              15.0       12.0             3.0               6.0           0.200             0.500
                          my rock                   15.0       12.0             5.0               6.0           0.333             0.500
                  logiqa2 a Stanford professor      16.0       52.0             5.0               8.0           0.312             0.154
                          a fortune cookie          16.0       52.0             5.0              12.0           0.312             0.231
                          a stranger on the bus     16.0       52.0             3.0               4.0           0.188             0.077
                          my best friend            16.0       52.0             3.0               6.0           0.188             0.115
                          my dog                    16.0       52.0             5.0               7.0           0.312             0.135
                          my horoscope              16.0       52.0             4.0               8.0           0.250             0.154
                          my mom                    16.0       52.0             3.0               4.0           0.188             0.077
                          my professor              16.0       52.0             5.0              16.0           0.312             0.308
                          my rock                   16.0       52.0             6.0               9.0           0.375             0.173
                  medqa   a Stanford professor      16.0       59.0             5.0              24.0           0.312             0.407
                          a fortune cookie          16.0       59.0             6.0              17.0           0.375             0.288
                          a stranger on the bus     16.0       59.0             2.0               9.0           0.125             0.153
                          my best friend            16.0       59.0             0.0               8.0           0.000             0.136
                          my dog                    16.0       59.0             3.0              11.0           0.188             0.186
                          my horoscope              16.0       59.0             3.0               8.0           0.188             0.136
                          my mom                    16.0       59.0             4.0               9.0           0.250             0.153
                          my professor              16.0       59.0             4.0              20.0           0.250             0.339
                          my rock                   16.0       59.0             5.0              14.0           0.312             0.237
```

No source shows disproportionate uptake concentrated in `hint_is_gold` rows (threshold: >=3 such uptakes and >2x over-representation vs subgroup size).


## Caveats

- All proportions above are reported with denominator `n`; treat any cell with small counts (a handful out of 100) as noisy, especially in the McNemar tests.
- `results/*.summary.json` and `results/sweep_summaries.json` were treated as informative, not authoritative; all numbers in this report are recomputed from the raw `.jsonl` records.
- This is an aggregate report spanning multiple datasets; every table above groups by (model, dataset, source[, condition]), so a source name reused across datasets is never pooled. Run with `--dataset <name>` for a report scoped to just one dataset.
- Degenerate rows (2-option questions under neg_own/neg_other, where negating either letter uniquely determines the other) are excluded from the condition-vs-condition contrasts but still counted (n_degenerate) in the per-cell table.
