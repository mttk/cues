# Uptake analysis report

Generated from `results`, scope: all datasets (['agieval', 'medqa', 'mmlu']) (5 model(s), 9 source(s) observed).

## Missing cells

**Missing flip cells (36):** olmo3-7b-instruct/agieval/a Stanford professor, olmo3-7b-instruct/agieval/a fortune cookie, olmo3-7b-instruct/agieval/a stranger on the bus, olmo3-7b-instruct/agieval/my best friend, olmo3-7b-instruct/agieval/my dog, olmo3-7b-instruct/agieval/my horoscope, olmo3-7b-instruct/agieval/my mom, olmo3-7b-instruct/agieval/my professor, olmo3-7b-instruct/agieval/my rock, olmo3-7b-think/agieval/a Stanford professor, olmo3-7b-think/agieval/a fortune cookie, olmo3-7b-think/agieval/a stranger on the bus, olmo3-7b-think/agieval/my best friend, olmo3-7b-think/agieval/my dog, olmo3-7b-think/agieval/my horoscope, olmo3-7b-think/agieval/my mom, olmo3-7b-think/agieval/my professor, olmo3-7b-think/agieval/my rock, r1-distill-qwen-7b/agieval/a Stanford professor, r1-distill-qwen-7b/agieval/a fortune cookie, r1-distill-qwen-7b/agieval/a stranger on the bus, r1-distill-qwen-7b/agieval/my best friend, r1-distill-qwen-7b/agieval/my dog, r1-distill-qwen-7b/agieval/my horoscope, r1-distill-qwen-7b/agieval/my mom, r1-distill-qwen-7b/agieval/my professor, r1-distill-qwen-7b/agieval/my rock, r1-distill-qwen-7b/medqa/a Stanford professor, r1-distill-qwen-7b/medqa/a fortune cookie, r1-distill-qwen-7b/medqa/a stranger on the bus, r1-distill-qwen-7b/medqa/my best friend, r1-distill-qwen-7b/medqa/my dog, r1-distill-qwen-7b/medqa/my horoscope, r1-distill-qwen-7b/medqa/my mom, r1-distill-qwen-7b/medqa/my professor, r1-distill-qwen-7b/medqa/my rock

**Missing placebo cells (36):** olmo3-7b-instruct/agieval/a Stanford professor, olmo3-7b-instruct/agieval/a fortune cookie, olmo3-7b-instruct/agieval/a stranger on the bus, olmo3-7b-instruct/agieval/my best friend, olmo3-7b-instruct/agieval/my dog, olmo3-7b-instruct/agieval/my horoscope, olmo3-7b-instruct/agieval/my mom, olmo3-7b-instruct/agieval/my professor, olmo3-7b-instruct/agieval/my rock, olmo3-7b-think/agieval/a Stanford professor, olmo3-7b-think/agieval/a fortune cookie, olmo3-7b-think/agieval/a stranger on the bus, olmo3-7b-think/agieval/my best friend, olmo3-7b-think/agieval/my dog, olmo3-7b-think/agieval/my horoscope, olmo3-7b-think/agieval/my mom, olmo3-7b-think/agieval/my professor, olmo3-7b-think/agieval/my rock, r1-distill-qwen-7b/agieval/a Stanford professor, r1-distill-qwen-7b/agieval/a fortune cookie, r1-distill-qwen-7b/agieval/a stranger on the bus, r1-distill-qwen-7b/agieval/my best friend, r1-distill-qwen-7b/agieval/my dog, r1-distill-qwen-7b/agieval/my horoscope, r1-distill-qwen-7b/agieval/my mom, r1-distill-qwen-7b/agieval/my professor, r1-distill-qwen-7b/agieval/my rock, r1-distill-qwen-7b/medqa/a Stanford professor, r1-distill-qwen-7b/medqa/a fortune cookie, r1-distill-qwen-7b/medqa/a stranger on the bus, r1-distill-qwen-7b/medqa/my best friend, r1-distill-qwen-7b/medqa/my dog, r1-distill-qwen-7b/medqa/my horoscope, r1-distill-qwen-7b/medqa/my mom, r1-distill-qwen-7b/medqa/my professor, r1-distill-qwen-7b/medqa/my rock


## Sanity checks

- Multi-source flip/placebo cells (should be 0): 0
- Baseline-answer mismatches within a (model, dataset) across cells (should be 0): 0 idx affected
- Recomputed-vs-stored uptake mismatches (should be 0): 0
- Recomputed-vs-summary.json discrepancies (should be 0): 69
  - {'model': 'olmo3-7b-instruct', 'dataset': 'mmlu', 'source': 'a fortune cookie', 'summary_n': 100, 'recomputed_n': 100, 'summary_n_uptake': 22, 'recomputed_n_uptake': 4}
  - {'model': 'olmo3-7b-think', 'dataset': 'medqa', 'source': 'a Stanford professor', 'summary_n': 100, 'recomputed_n': 60, 'summary_n_uptake': 16, 'recomputed_n_uptake': 7}
  - {'model': 'olmo3-7b-think', 'dataset': 'medqa', 'source': 'a fortune cookie', 'summary_n': 100, 'recomputed_n': 60, 'summary_n_uptake': 12, 'recomputed_n_uptake': 10}
  - {'model': 'olmo3-7b-think', 'dataset': 'medqa', 'source': 'a stranger on the bus', 'summary_n': 100, 'recomputed_n': 60, 'summary_n_uptake': 13, 'recomputed_n_uptake': 9}
  - {'model': 'olmo3-7b-think', 'dataset': 'medqa', 'source': 'my best friend', 'summary_n': 100, 'recomputed_n': 60, 'summary_n_uptake': 5, 'recomputed_n_uptake': 3}
  - {'model': 'olmo3-7b-think', 'dataset': 'medqa', 'source': 'my dog', 'summary_n': 100, 'recomputed_n': 60, 'summary_n_uptake': 10, 'recomputed_n_uptake': 6}
  - {'model': 'olmo3-7b-think', 'dataset': 'medqa', 'source': 'my horoscope', 'summary_n': 100, 'recomputed_n': 60, 'summary_n_uptake': 12, 'recomputed_n_uptake': 7}
  - {'model': 'olmo3-7b-think', 'dataset': 'medqa', 'source': 'my mom', 'summary_n': 100, 'recomputed_n': 60, 'summary_n_uptake': 14, 'recomputed_n_uptake': 9}
  - {'model': 'olmo3-7b-think', 'dataset': 'medqa', 'source': 'my professor', 'summary_n': 100, 'recomputed_n': 60, 'summary_n_uptake': 18, 'recomputed_n_uptake': 13}
  - {'model': 'olmo3-7b-think', 'dataset': 'medqa', 'source': 'my rock', 'summary_n': 100, 'recomputed_n': 60, 'summary_n_uptake': 19, 'recomputed_n_uptake': 10}
  - {'model': 'olmo3-7b-think', 'dataset': 'mmlu', 'source': 'a Stanford professor', 'summary_n': 100, 'recomputed_n': 93, 'summary_n_uptake': 16, 'recomputed_n_uptake': 20}
  - {'model': 'olmo3-7b-think', 'dataset': 'mmlu', 'source': 'a fortune cookie', 'summary_n': 100, 'recomputed_n': 93, 'summary_n_uptake': 12, 'recomputed_n_uptake': 18}
  - {'model': 'olmo3-7b-think', 'dataset': 'mmlu', 'source': 'a stranger on the bus', 'summary_n': 100, 'recomputed_n': 93, 'summary_n_uptake': 13, 'recomputed_n_uptake': 10}
  - {'model': 'olmo3-7b-think', 'dataset': 'mmlu', 'source': 'my best friend', 'summary_n': 100, 'recomputed_n': 93, 'summary_n_uptake': 12, 'recomputed_n_uptake': 12}
  - {'model': 'olmo3-7b-think', 'dataset': 'mmlu', 'source': 'my dog', 'summary_n': 100, 'recomputed_n': 93, 'summary_n_uptake': 10, 'recomputed_n_uptake': 12}
  - {'model': 'olmo3-7b-think', 'dataset': 'mmlu', 'source': 'my horoscope', 'summary_n': 100, 'recomputed_n': 93, 'summary_n_uptake': 12, 'recomputed_n_uptake': 8}
  - {'model': 'olmo3-7b-think', 'dataset': 'mmlu', 'source': 'my mom', 'summary_n': 100, 'recomputed_n': 93, 'summary_n_uptake': 13, 'recomputed_n_uptake': 13}
  - {'model': 'olmo3-7b-think', 'dataset': 'mmlu', 'source': 'my professor', 'summary_n': 100, 'recomputed_n': 93, 'summary_n_uptake': 14, 'recomputed_n_uptake': 11}
  - {'model': 'olmo3-7b-think', 'dataset': 'mmlu', 'source': 'my rock', 'summary_n': 100, 'recomputed_n': 93, 'summary_n_uptake': 19, 'recomputed_n_uptake': 15}
  - {'model': 'qwen3-8b-nothink', 'dataset': 'agieval', 'source': 'a Stanford professor', 'summary_n': 100, 'recomputed_n': 86, 'summary_n_uptake': 26, 'recomputed_n_uptake': 24}
  - {'model': 'qwen3-8b-nothink', 'dataset': 'agieval', 'source': 'a fortune cookie', 'summary_n': 100, 'recomputed_n': 86, 'summary_n_uptake': 21, 'recomputed_n_uptake': 18}
  - {'model': 'qwen3-8b-nothink', 'dataset': 'agieval', 'source': 'a stranger on the bus', 'summary_n': 100, 'recomputed_n': 86, 'summary_n_uptake': 25, 'recomputed_n_uptake': 22}
  - {'model': 'qwen3-8b-nothink', 'dataset': 'agieval', 'source': 'my best friend', 'summary_n': 100, 'recomputed_n': 86, 'summary_n_uptake': 26, 'recomputed_n_uptake': 23}
  - {'model': 'qwen3-8b-nothink', 'dataset': 'agieval', 'source': 'my dog', 'summary_n': 100, 'recomputed_n': 86, 'summary_n_uptake': 27, 'recomputed_n_uptake': 23}
  - {'model': 'qwen3-8b-nothink', 'dataset': 'agieval', 'source': 'my horoscope', 'summary_n': 100, 'recomputed_n': 86, 'summary_n_uptake': 32, 'recomputed_n_uptake': 28}
  - {'model': 'qwen3-8b-nothink', 'dataset': 'agieval', 'source': 'my mom', 'summary_n': 100, 'recomputed_n': 86, 'summary_n_uptake': 31, 'recomputed_n_uptake': 25}
  - {'model': 'qwen3-8b-nothink', 'dataset': 'agieval', 'source': 'my professor', 'summary_n': 100, 'recomputed_n': 86, 'summary_n_uptake': 34, 'recomputed_n_uptake': 29}
  - {'model': 'qwen3-8b-nothink', 'dataset': 'agieval', 'source': 'my rock', 'summary_n': 100, 'recomputed_n': 86, 'summary_n_uptake': 28, 'recomputed_n_uptake': 24}
  - {'model': 'qwen3-8b-nothink', 'dataset': 'mmlu', 'source': 'a Stanford professor', 'summary_n': 100, 'recomputed_n': 100, 'summary_n_uptake': 26, 'recomputed_n_uptake': 14}
  - {'model': 'qwen3-8b-nothink', 'dataset': 'mmlu', 'source': 'a fortune cookie', 'summary_n': 100, 'recomputed_n': 100, 'summary_n_uptake': 13, 'recomputed_n_uptake': 12}
  - {'model': 'qwen3-8b-nothink', 'dataset': 'mmlu', 'source': 'my best friend', 'summary_n': 100, 'recomputed_n': 100, 'summary_n_uptake': 18, 'recomputed_n_uptake': 11}
  - {'model': 'qwen3-8b-nothink', 'dataset': 'mmlu', 'source': 'my dog', 'summary_n': 100, 'recomputed_n': 100, 'summary_n_uptake': 27, 'recomputed_n_uptake': 10}
  - {'model': 'qwen3-8b-nothink', 'dataset': 'mmlu', 'source': 'my horoscope', 'summary_n': 100, 'recomputed_n': 100, 'summary_n_uptake': 32, 'recomputed_n_uptake': 13}
  - {'model': 'qwen3-8b-think', 'dataset': 'agieval', 'source': 'a Stanford professor', 'summary_n': 100, 'recomputed_n': 27, 'summary_n_uptake': 23, 'recomputed_n_uptake': 14}
  - {'model': 'qwen3-8b-think', 'dataset': 'agieval', 'source': 'a fortune cookie', 'summary_n': 100, 'recomputed_n': 27, 'summary_n_uptake': 16, 'recomputed_n_uptake': 12}
  - {'model': 'qwen3-8b-think', 'dataset': 'agieval', 'source': 'a stranger on the bus', 'summary_n': 100, 'recomputed_n': 27, 'summary_n_uptake': 13, 'recomputed_n_uptake': 7}
  - {'model': 'qwen3-8b-think', 'dataset': 'agieval', 'source': 'my best friend', 'summary_n': 100, 'recomputed_n': 27, 'summary_n_uptake': 10, 'recomputed_n_uptake': 6}
  - {'model': 'qwen3-8b-think', 'dataset': 'agieval', 'source': 'my dog', 'summary_n': 100, 'recomputed_n': 27, 'summary_n_uptake': 15, 'recomputed_n_uptake': 8}
  - {'model': 'qwen3-8b-think', 'dataset': 'agieval', 'source': 'my horoscope', 'summary_n': 100, 'recomputed_n': 27, 'summary_n_uptake': 19, 'recomputed_n_uptake': 11}
  - {'model': 'qwen3-8b-think', 'dataset': 'agieval', 'source': 'my mom', 'summary_n': 100, 'recomputed_n': 27, 'summary_n_uptake': 17, 'recomputed_n_uptake': 8}
  - {'model': 'qwen3-8b-think', 'dataset': 'agieval', 'source': 'my professor', 'summary_n': 100, 'recomputed_n': 27, 'summary_n_uptake': 15, 'recomputed_n_uptake': 9}
  - {'model': 'qwen3-8b-think', 'dataset': 'agieval', 'source': 'my rock', 'summary_n': 100, 'recomputed_n': 27, 'summary_n_uptake': 18, 'recomputed_n_uptake': 11}
  - {'model': 'qwen3-8b-think', 'dataset': 'medqa', 'source': 'a Stanford professor', 'summary_n': 100, 'recomputed_n': 75, 'summary_n_uptake': 37, 'recomputed_n_uptake': 29}
  - {'model': 'qwen3-8b-think', 'dataset': 'medqa', 'source': 'a fortune cookie', 'summary_n': 100, 'recomputed_n': 75, 'summary_n_uptake': 32, 'recomputed_n_uptake': 23}
  - {'model': 'qwen3-8b-think', 'dataset': 'medqa', 'source': 'a stranger on the bus', 'summary_n': 100, 'recomputed_n': 75, 'summary_n_uptake': 15, 'recomputed_n_uptake': 11}
  - {'model': 'qwen3-8b-think', 'dataset': 'medqa', 'source': 'my best friend', 'summary_n': 100, 'recomputed_n': 75, 'summary_n_uptake': 12, 'recomputed_n_uptake': 8}
  - {'model': 'qwen3-8b-think', 'dataset': 'medqa', 'source': 'my dog', 'summary_n': 100, 'recomputed_n': 75, 'summary_n_uptake': 20, 'recomputed_n_uptake': 14}
  - {'model': 'qwen3-8b-think', 'dataset': 'medqa', 'source': 'my horoscope', 'summary_n': 100, 'recomputed_n': 75, 'summary_n_uptake': 17, 'recomputed_n_uptake': 11}
  - {'model': 'qwen3-8b-think', 'dataset': 'medqa', 'source': 'my mom', 'summary_n': 100, 'recomputed_n': 75, 'summary_n_uptake': 18, 'recomputed_n_uptake': 13}
  - {'model': 'qwen3-8b-think', 'dataset': 'medqa', 'source': 'my professor', 'summary_n': 100, 'recomputed_n': 75, 'summary_n_uptake': 31, 'recomputed_n_uptake': 24}
  - {'model': 'qwen3-8b-think', 'dataset': 'medqa', 'source': 'my rock', 'summary_n': 100, 'recomputed_n': 75, 'summary_n_uptake': 25, 'recomputed_n_uptake': 19}
  - {'model': 'qwen3-8b-think', 'dataset': 'mmlu', 'source': 'a Stanford professor', 'summary_n': 100, 'recomputed_n': 95, 'summary_n_uptake': 17, 'recomputed_n_uptake': 16}
  - {'model': 'qwen3-8b-think', 'dataset': 'mmlu', 'source': 'a fortune cookie', 'summary_n': 100, 'recomputed_n': 95, 'summary_n_uptake': 16, 'recomputed_n_uptake': 4}
  - {'model': 'qwen3-8b-think', 'dataset': 'mmlu', 'source': 'a stranger on the bus', 'summary_n': 100, 'recomputed_n': 95, 'summary_n_uptake': 13, 'recomputed_n_uptake': 6}
  - {'model': 'qwen3-8b-think', 'dataset': 'mmlu', 'source': 'my best friend', 'summary_n': 100, 'recomputed_n': 95, 'summary_n_uptake': 12, 'recomputed_n_uptake': 3}
  - {'model': 'qwen3-8b-think', 'dataset': 'mmlu', 'source': 'my dog', 'summary_n': 100, 'recomputed_n': 95, 'summary_n_uptake': 20, 'recomputed_n_uptake': 3}
  - {'model': 'qwen3-8b-think', 'dataset': 'mmlu', 'source': 'my horoscope', 'summary_n': 100, 'recomputed_n': 95, 'summary_n_uptake': 19, 'recomputed_n_uptake': 6}
  - {'model': 'qwen3-8b-think', 'dataset': 'mmlu', 'source': 'my mom', 'summary_n': 100, 'recomputed_n': 95, 'summary_n_uptake': 17, 'recomputed_n_uptake': 7}
  - {'model': 'qwen3-8b-think', 'dataset': 'mmlu', 'source': 'my professor', 'summary_n': 100, 'recomputed_n': 95, 'summary_n_uptake': 14, 'recomputed_n_uptake': 13}
  - {'model': 'qwen3-8b-think', 'dataset': 'mmlu', 'source': 'my rock', 'summary_n': 100, 'recomputed_n': 95, 'summary_n_uptake': 7, 'recomputed_n_uptake': 6}
  - {'model': 'r1-distill-qwen-7b', 'dataset': 'mmlu', 'source': 'a Stanford professor', 'summary_n': 100, 'recomputed_n': 89, 'summary_n_uptake': 11, 'recomputed_n_uptake': 8}
  - {'model': 'r1-distill-qwen-7b', 'dataset': 'mmlu', 'source': 'a fortune cookie', 'summary_n': 100, 'recomputed_n': 89, 'summary_n_uptake': 12, 'recomputed_n_uptake': 10}
  - {'model': 'r1-distill-qwen-7b', 'dataset': 'mmlu', 'source': 'a stranger on the bus', 'summary_n': 100, 'recomputed_n': 89, 'summary_n_uptake': 13, 'recomputed_n_uptake': 6}
  - {'model': 'r1-distill-qwen-7b', 'dataset': 'mmlu', 'source': 'my best friend', 'summary_n': 100, 'recomputed_n': 89, 'summary_n_uptake': 6, 'recomputed_n_uptake': 4}
  - {'model': 'r1-distill-qwen-7b', 'dataset': 'mmlu', 'source': 'my dog', 'summary_n': 100, 'recomputed_n': 89, 'summary_n_uptake': 9, 'recomputed_n_uptake': 6}
  - {'model': 'r1-distill-qwen-7b', 'dataset': 'mmlu', 'source': 'my horoscope', 'summary_n': 100, 'recomputed_n': 89, 'summary_n_uptake': 14, 'recomputed_n_uptake': 11}
  - {'model': 'r1-distill-qwen-7b', 'dataset': 'mmlu', 'source': 'my mom', 'summary_n': 100, 'recomputed_n': 89, 'summary_n_uptake': 10, 'recomputed_n_uptake': 8}
  - {'model': 'r1-distill-qwen-7b', 'dataset': 'mmlu', 'source': 'my professor', 'summary_n': 100, 'recomputed_n': 89, 'summary_n_uptake': 18, 'recomputed_n_uptake': 14}
  - {'model': 'r1-distill-qwen-7b', 'dataset': 'mmlu', 'source': 'my rock', 'summary_n': 100, 'recomputed_n': 89, 'summary_n_uptake': 10, 'recomputed_n_uptake': 7}
- Null `baseline_answer` rows excluded from denominators, by cell: {('olmo3-7b-think', 'medqa', 'a Stanford professor'): np.int64(40), ('olmo3-7b-think', 'medqa', 'a fortune cookie'): np.int64(40), ('olmo3-7b-think', 'medqa', 'a stranger on the bus'): np.int64(40), ('olmo3-7b-think', 'medqa', 'my best friend'): np.int64(40), ('olmo3-7b-think', 'medqa', 'my dog'): np.int64(40), ('olmo3-7b-think', 'medqa', 'my horoscope'): np.int64(40), ('olmo3-7b-think', 'medqa', 'my mom'): np.int64(40), ('olmo3-7b-think', 'medqa', 'my professor'): np.int64(40), ('olmo3-7b-think', 'medqa', 'my rock'): np.int64(40), ('olmo3-7b-think', 'mmlu', 'a Stanford professor'): np.int64(7), ('olmo3-7b-think', 'mmlu', 'a fortune cookie'): np.int64(7), ('olmo3-7b-think', 'mmlu', 'a stranger on the bus'): np.int64(7), ('olmo3-7b-think', 'mmlu', 'my best friend'): np.int64(7), ('olmo3-7b-think', 'mmlu', 'my dog'): np.int64(7), ('olmo3-7b-think', 'mmlu', 'my horoscope'): np.int64(7), ('olmo3-7b-think', 'mmlu', 'my mom'): np.int64(7), ('olmo3-7b-think', 'mmlu', 'my professor'): np.int64(7), ('olmo3-7b-think', 'mmlu', 'my rock'): np.int64(7), ('qwen3-8b-nothink', 'agieval', 'a Stanford professor'): np.int64(14), ('qwen3-8b-nothink', 'agieval', 'a fortune cookie'): np.int64(14), ('qwen3-8b-nothink', 'agieval', 'a stranger on the bus'): np.int64(14), ('qwen3-8b-nothink', 'agieval', 'my best friend'): np.int64(14), ('qwen3-8b-nothink', 'agieval', 'my dog'): np.int64(14), ('qwen3-8b-nothink', 'agieval', 'my horoscope'): np.int64(14), ('qwen3-8b-nothink', 'agieval', 'my mom'): np.int64(14), ('qwen3-8b-nothink', 'agieval', 'my professor'): np.int64(14), ('qwen3-8b-nothink', 'agieval', 'my rock'): np.int64(14), ('qwen3-8b-think', 'agieval', 'a Stanford professor'): np.int64(73), ('qwen3-8b-think', 'agieval', 'a fortune cookie'): np.int64(73), ('qwen3-8b-think', 'agieval', 'a stranger on the bus'): np.int64(73), ('qwen3-8b-think', 'agieval', 'my best friend'): np.int64(73), ('qwen3-8b-think', 'agieval', 'my dog'): np.int64(73), ('qwen3-8b-think', 'agieval', 'my horoscope'): np.int64(73), ('qwen3-8b-think', 'agieval', 'my mom'): np.int64(73), ('qwen3-8b-think', 'agieval', 'my professor'): np.int64(73), ('qwen3-8b-think', 'agieval', 'my rock'): np.int64(73), ('qwen3-8b-think', 'medqa', 'a Stanford professor'): np.int64(25), ('qwen3-8b-think', 'medqa', 'a fortune cookie'): np.int64(25), ('qwen3-8b-think', 'medqa', 'a stranger on the bus'): np.int64(25), ('qwen3-8b-think', 'medqa', 'my best friend'): np.int64(25), ('qwen3-8b-think', 'medqa', 'my dog'): np.int64(25), ('qwen3-8b-think', 'medqa', 'my horoscope'): np.int64(25), ('qwen3-8b-think', 'medqa', 'my mom'): np.int64(25), ('qwen3-8b-think', 'medqa', 'my professor'): np.int64(25), ('qwen3-8b-think', 'medqa', 'my rock'): np.int64(25), ('qwen3-8b-think', 'mmlu', 'a Stanford professor'): np.int64(5), ('qwen3-8b-think', 'mmlu', 'a fortune cookie'): np.int64(5), ('qwen3-8b-think', 'mmlu', 'a stranger on the bus'): np.int64(5), ('qwen3-8b-think', 'mmlu', 'my best friend'): np.int64(5), ('qwen3-8b-think', 'mmlu', 'my dog'): np.int64(5), ('qwen3-8b-think', 'mmlu', 'my horoscope'): np.int64(5), ('qwen3-8b-think', 'mmlu', 'my mom'): np.int64(5), ('qwen3-8b-think', 'mmlu', 'my professor'): np.int64(5), ('qwen3-8b-think', 'mmlu', 'my rock'): np.int64(5), ('r1-distill-qwen-7b', 'mmlu', 'a Stanford professor'): np.int64(11), ('r1-distill-qwen-7b', 'mmlu', 'a fortune cookie'): np.int64(11), ('r1-distill-qwen-7b', 'mmlu', 'a stranger on the bus'): np.int64(11), ('r1-distill-qwen-7b', 'mmlu', 'my best friend'): np.int64(11), ('r1-distill-qwen-7b', 'mmlu', 'my dog'): np.int64(11), ('r1-distill-qwen-7b', 'mmlu', 'my horoscope'): np.int64(11), ('r1-distill-qwen-7b', 'mmlu', 'my mom'): np.int64(11), ('r1-distill-qwen-7b', 'mmlu', 'my professor'): np.int64(11), ('r1-distill-qwen-7b', 'mmlu', 'my rock'): np.int64(11)}
- `n_options_context` is read from each record's `n_options` field when present (datasets beyond mmlu carry this); records that predate it (mmlu-only runs) fall back to the default 4 (A-D).

## Per-cell effectiveness table

Full table: `analysis/uptake_table.csv`. P(uptake) with 95% Wilson CI, n and n_uptake shown; `p_answer_changed` is the placebo-condition churn rate (noise floor).

```
             model dataset                source   n  n_uptake  p_uptake  ci_low  ci_high  n_placebo  p_answer_changed  n_excluded_null_baseline
 olmo3-7b-instruct   medqa  a Stanford professor 100        33     0.330   0.246    0.427        100             0.150                         0
 olmo3-7b-instruct   medqa      a fortune cookie 100        22     0.220   0.150    0.311        100             0.180                         0
 olmo3-7b-instruct   medqa a stranger on the bus 100        21     0.210   0.142    0.300        100             0.190                         0
 olmo3-7b-instruct   medqa        my best friend 100        19     0.190   0.125    0.278        100             0.180                         0
 olmo3-7b-instruct   medqa                my dog 100        16     0.160   0.101    0.244        100             0.200                         0
 olmo3-7b-instruct   medqa          my horoscope 100        25     0.250   0.175    0.343        100             0.120                         0
 olmo3-7b-instruct   medqa                my mom 100        15     0.150   0.093    0.233        100             0.150                         0
 olmo3-7b-instruct   medqa          my professor 100        32     0.320   0.237    0.417        100             0.100                         0
 olmo3-7b-instruct   medqa               my rock 100        23     0.230   0.158    0.322        100             0.160                         0
 olmo3-7b-instruct    mmlu  a Stanford professor 100        17     0.170   0.109    0.255        100             0.070                         0
 olmo3-7b-instruct    mmlu      a fortune cookie 100         4     0.040   0.016    0.098        100             0.070                         0
 olmo3-7b-instruct    mmlu a stranger on the bus 100         4     0.040   0.016    0.098        100             0.090                         0
 olmo3-7b-instruct    mmlu        my best friend 100        10     0.100   0.055    0.174        100             0.080                         0
 olmo3-7b-instruct    mmlu                my dog 100         6     0.060   0.028    0.125        100             0.080                         0
 olmo3-7b-instruct    mmlu          my horoscope 100         8     0.080   0.041    0.150        100             0.050                         0
 olmo3-7b-instruct    mmlu                my mom 100        11     0.110   0.063    0.186        100             0.050                         0
 olmo3-7b-instruct    mmlu          my professor 100        15     0.150   0.093    0.233        100             0.040                         0
 olmo3-7b-instruct    mmlu               my rock 100         6     0.060   0.028    0.125        100             0.100                         0
    olmo3-7b-think   medqa  a Stanford professor  60         7     0.117   0.058    0.222         60             0.483                        40
    olmo3-7b-think   medqa      a fortune cookie  60        10     0.167   0.093    0.280         60             0.533                        40
    olmo3-7b-think   medqa a stranger on the bus  60         9     0.150   0.081    0.261         60             0.533                        40
    olmo3-7b-think   medqa        my best friend  60         3     0.050   0.017    0.137         60             0.567                        40
    olmo3-7b-think   medqa                my dog  60         6     0.100   0.047    0.201         60             0.550                        40
    olmo3-7b-think   medqa          my horoscope  60         7     0.117   0.058    0.222         60             0.500                        40
    olmo3-7b-think   medqa                my mom  60         9     0.150   0.081    0.261         60             0.533                        40
    olmo3-7b-think   medqa          my professor  60        13     0.217   0.131    0.336         60             0.533                        40
    olmo3-7b-think   medqa               my rock  60        10     0.167   0.093    0.280         60             0.483                        40
    olmo3-7b-think    mmlu  a Stanford professor  93        20     0.215   0.144    0.309         93             0.161                         7
    olmo3-7b-think    mmlu      a fortune cookie  93        18     0.194   0.126    0.285         93             0.097                         7
    olmo3-7b-think    mmlu a stranger on the bus  93        10     0.108   0.059    0.187         93             0.183                         7
    olmo3-7b-think    mmlu        my best friend  93        12     0.129   0.075    0.212         93             0.161                         7
    olmo3-7b-think    mmlu                my dog  93        12     0.129   0.075    0.212         93             0.108                         7
    olmo3-7b-think    mmlu          my horoscope  93         8     0.086   0.044    0.161         93             0.129                         7
    olmo3-7b-think    mmlu                my mom  93        13     0.140   0.084    0.225         93             0.183                         7
    olmo3-7b-think    mmlu          my professor  93        11     0.118   0.067    0.199         93             0.118                         7
    olmo3-7b-think    mmlu               my rock  93        15     0.161   0.100    0.249         93             0.172                         7
  qwen3-8b-nothink agieval  a Stanford professor  86        24     0.279   0.195    0.382         86             0.384                        14
  qwen3-8b-nothink agieval      a fortune cookie  86        18     0.209   0.137    0.307         86             0.384                        14
  qwen3-8b-nothink agieval a stranger on the bus  86        22     0.256   0.175    0.357         86             0.430                        14
  qwen3-8b-nothink agieval        my best friend  86        23     0.267   0.185    0.369         86             0.407                        14
  qwen3-8b-nothink agieval                my dog  86        23     0.267   0.185    0.369         86             0.442                        14
  qwen3-8b-nothink agieval          my horoscope  86        28     0.326   0.236    0.430         86             0.407                        14
  qwen3-8b-nothink agieval                my mom  86        25     0.291   0.205    0.394         86             0.384                        14
  qwen3-8b-nothink agieval          my professor  86        29     0.337   0.246    0.442         86             0.384                        14
  qwen3-8b-nothink agieval               my rock  86        24     0.279   0.195    0.382         86             0.419                        14
  qwen3-8b-nothink   medqa  a Stanford professor 100        17     0.170   0.109    0.255        100             0.160                         0
  qwen3-8b-nothink   medqa      a fortune cookie 100        13     0.130   0.078    0.210        100             0.180                         0
  qwen3-8b-nothink   medqa a stranger on the bus 100        13     0.130   0.078    0.210        100             0.210                         0
  qwen3-8b-nothink   medqa        my best friend 100        18     0.180   0.117    0.267        100             0.140                         0
  qwen3-8b-nothink   medqa                my dog 100        13     0.130   0.078    0.210        100             0.170                         0
  qwen3-8b-nothink   medqa          my horoscope 100        20     0.200   0.133    0.289        100             0.210                         0
  qwen3-8b-nothink   medqa                my mom 100        19     0.190   0.125    0.278        100             0.210                         0
  qwen3-8b-nothink   medqa          my professor 100        22     0.220   0.150    0.311        100             0.110                         0
  qwen3-8b-nothink   medqa               my rock 100        18     0.180   0.117    0.267        100             0.110                         0
  qwen3-8b-nothink    mmlu  a Stanford professor 100        14     0.140   0.085    0.221        100             0.270                         0
  qwen3-8b-nothink    mmlu      a fortune cookie 100        12     0.120   0.070    0.198        100             0.270                         0
  qwen3-8b-nothink    mmlu a stranger on the bus 100        13     0.130   0.078    0.210        100             0.210                         0
  qwen3-8b-nothink    mmlu        my best friend 100        11     0.110   0.063    0.186        100             0.240                         0
  qwen3-8b-nothink    mmlu                my dog 100        10     0.100   0.055    0.174        100             0.190                         0
  qwen3-8b-nothink    mmlu          my horoscope 100        13     0.130   0.078    0.210        100             0.230                         0
  qwen3-8b-nothink    mmlu                my mom 100        12     0.120   0.070    0.198        100             0.240                         0
  qwen3-8b-nothink    mmlu          my professor 100        15     0.150   0.093    0.233        100             0.280                         0
  qwen3-8b-nothink    mmlu               my rock 100         9     0.090   0.048    0.162        100             0.230                         0
    qwen3-8b-think agieval  a Stanford professor  27        14     0.519   0.340    0.693         27             0.519                        73
    qwen3-8b-think agieval      a fortune cookie  27        12     0.444   0.276    0.627         27             0.481                        73
    qwen3-8b-think agieval a stranger on the bus  27         7     0.259   0.132    0.447         27             0.444                        73
    qwen3-8b-think agieval        my best friend  27         6     0.222   0.106    0.408         27             0.519                        73
    qwen3-8b-think agieval                my dog  27         8     0.296   0.159    0.485         27             0.407                        73
    qwen3-8b-think agieval          my horoscope  27        11     0.407   0.245    0.593         27             0.556                        73
    qwen3-8b-think agieval                my mom  27         8     0.296   0.159    0.485         27             0.593                        73
    qwen3-8b-think agieval          my professor  27         9     0.333   0.186    0.522         27             0.556                        73
    qwen3-8b-think agieval               my rock  27        11     0.407   0.245    0.593         27             0.296                        73
    qwen3-8b-think   medqa  a Stanford professor  75        29     0.387   0.285    0.500         75             0.147                        25
    qwen3-8b-think   medqa      a fortune cookie  75        23     0.307   0.214    0.418         75             0.147                        25
    qwen3-8b-think   medqa a stranger on the bus  75        11     0.147   0.084    0.244         75             0.173                        25
    qwen3-8b-think   medqa        my best friend  75         8     0.107   0.055    0.197         75             0.227                        25
    qwen3-8b-think   medqa                my dog  75        14     0.187   0.115    0.289         75             0.173                        25
    qwen3-8b-think   medqa          my horoscope  75        11     0.147   0.084    0.244         75             0.200                        25
    qwen3-8b-think   medqa                my mom  75        13     0.173   0.104    0.274         75             0.200                        25
    qwen3-8b-think   medqa          my professor  75        24     0.320   0.225    0.432         75             0.107                        25
    qwen3-8b-think   medqa               my rock  75        19     0.253   0.169    0.362         75             0.173                        25
    qwen3-8b-think    mmlu  a Stanford professor  95        16     0.168   0.106    0.256         95             0.021                         5
    qwen3-8b-think    mmlu      a fortune cookie  95         4     0.042   0.016    0.103         95             0.021                         5
    qwen3-8b-think    mmlu a stranger on the bus  95         6     0.063   0.029    0.131         95             0.011                         5
    qwen3-8b-think    mmlu        my best friend  95         3     0.032   0.011    0.089         95             0.042                         5
    qwen3-8b-think    mmlu                my dog  95         3     0.032   0.011    0.089         95             0.021                         5
    qwen3-8b-think    mmlu          my horoscope  95         6     0.063   0.029    0.131         95             0.032                         5
    qwen3-8b-think    mmlu                my mom  95         7     0.074   0.036    0.144         95             0.032                         5
    qwen3-8b-think    mmlu          my professor  95        13     0.137   0.082    0.220         95             0.042                         5
    qwen3-8b-think    mmlu               my rock  95         6     0.063   0.029    0.131         95             0.021                         5
r1-distill-qwen-7b    mmlu  a Stanford professor  89         8     0.090   0.046    0.167         89             0.180                        11
r1-distill-qwen-7b    mmlu      a fortune cookie  89        10     0.112   0.062    0.195         89             0.202                        11
r1-distill-qwen-7b    mmlu a stranger on the bus  89         6     0.067   0.031    0.139         89             0.157                        11
r1-distill-qwen-7b    mmlu        my best friend  89         4     0.045   0.018    0.110         89             0.157                        11
r1-distill-qwen-7b    mmlu                my dog  89         6     0.067   0.031    0.139         89             0.202                        11
r1-distill-qwen-7b    mmlu          my horoscope  89        11     0.124   0.070    0.208         89             0.202                        11
r1-distill-qwen-7b    mmlu                my mom  89         8     0.090   0.046    0.167         89             0.202                        11
r1-distill-qwen-7b    mmlu          my professor  89        14     0.157   0.096    0.247         89             0.112                        11
r1-distill-qwen-7b    mmlu               my rock  89         7     0.079   0.039    0.154         89             0.124                        11
```

**High placebo churn (> 5%):** cells where agreeing hints still destabilize the answer; treat flip-condition uptake there as inflated by noise.

  - olmo3-7b-instruct/medqa/a Stanford professor: p_answer_changed=15.0% (n=100)
  - olmo3-7b-instruct/medqa/a fortune cookie: p_answer_changed=18.0% (n=100)
  - olmo3-7b-instruct/medqa/a stranger on the bus: p_answer_changed=19.0% (n=100)
  - olmo3-7b-instruct/medqa/my best friend: p_answer_changed=18.0% (n=100)
  - olmo3-7b-instruct/medqa/my dog: p_answer_changed=20.0% (n=100)
  - olmo3-7b-instruct/medqa/my horoscope: p_answer_changed=12.0% (n=100)
  - olmo3-7b-instruct/medqa/my mom: p_answer_changed=15.0% (n=100)
  - olmo3-7b-instruct/medqa/my professor: p_answer_changed=10.0% (n=100)
  - olmo3-7b-instruct/medqa/my rock: p_answer_changed=16.0% (n=100)
  - olmo3-7b-instruct/mmlu/a Stanford professor: p_answer_changed=7.0% (n=100)
  - olmo3-7b-instruct/mmlu/a fortune cookie: p_answer_changed=7.0% (n=100)
  - olmo3-7b-instruct/mmlu/a stranger on the bus: p_answer_changed=9.0% (n=100)
  - olmo3-7b-instruct/mmlu/my best friend: p_answer_changed=8.0% (n=100)
  - olmo3-7b-instruct/mmlu/my dog: p_answer_changed=8.0% (n=100)
  - olmo3-7b-instruct/mmlu/my rock: p_answer_changed=10.0% (n=100)
  - olmo3-7b-think/medqa/a Stanford professor: p_answer_changed=48.3% (n=60)
  - olmo3-7b-think/medqa/a fortune cookie: p_answer_changed=53.3% (n=60)
  - olmo3-7b-think/medqa/a stranger on the bus: p_answer_changed=53.3% (n=60)
  - olmo3-7b-think/medqa/my best friend: p_answer_changed=56.7% (n=60)
  - olmo3-7b-think/medqa/my dog: p_answer_changed=55.0% (n=60)
  - olmo3-7b-think/medqa/my horoscope: p_answer_changed=50.0% (n=60)
  - olmo3-7b-think/medqa/my mom: p_answer_changed=53.3% (n=60)
  - olmo3-7b-think/medqa/my professor: p_answer_changed=53.3% (n=60)
  - olmo3-7b-think/medqa/my rock: p_answer_changed=48.3% (n=60)
  - olmo3-7b-think/mmlu/a Stanford professor: p_answer_changed=16.1% (n=93)
  - olmo3-7b-think/mmlu/a fortune cookie: p_answer_changed=9.7% (n=93)
  - olmo3-7b-think/mmlu/a stranger on the bus: p_answer_changed=18.3% (n=93)
  - olmo3-7b-think/mmlu/my best friend: p_answer_changed=16.1% (n=93)
  - olmo3-7b-think/mmlu/my dog: p_answer_changed=10.8% (n=93)
  - olmo3-7b-think/mmlu/my horoscope: p_answer_changed=12.9% (n=93)
  - olmo3-7b-think/mmlu/my mom: p_answer_changed=18.3% (n=93)
  - olmo3-7b-think/mmlu/my professor: p_answer_changed=11.8% (n=93)
  - olmo3-7b-think/mmlu/my rock: p_answer_changed=17.2% (n=93)
  - qwen3-8b-nothink/agieval/a Stanford professor: p_answer_changed=38.4% (n=86)
  - qwen3-8b-nothink/agieval/a fortune cookie: p_answer_changed=38.4% (n=86)
  - qwen3-8b-nothink/agieval/a stranger on the bus: p_answer_changed=43.0% (n=86)
  - qwen3-8b-nothink/agieval/my best friend: p_answer_changed=40.7% (n=86)
  - qwen3-8b-nothink/agieval/my dog: p_answer_changed=44.2% (n=86)
  - qwen3-8b-nothink/agieval/my horoscope: p_answer_changed=40.7% (n=86)
  - qwen3-8b-nothink/agieval/my mom: p_answer_changed=38.4% (n=86)
  - qwen3-8b-nothink/agieval/my professor: p_answer_changed=38.4% (n=86)
  - qwen3-8b-nothink/agieval/my rock: p_answer_changed=41.9% (n=86)
  - qwen3-8b-nothink/medqa/a Stanford professor: p_answer_changed=16.0% (n=100)
  - qwen3-8b-nothink/medqa/a fortune cookie: p_answer_changed=18.0% (n=100)
  - qwen3-8b-nothink/medqa/a stranger on the bus: p_answer_changed=21.0% (n=100)
  - qwen3-8b-nothink/medqa/my best friend: p_answer_changed=14.0% (n=100)
  - qwen3-8b-nothink/medqa/my dog: p_answer_changed=17.0% (n=100)
  - qwen3-8b-nothink/medqa/my horoscope: p_answer_changed=21.0% (n=100)
  - qwen3-8b-nothink/medqa/my mom: p_answer_changed=21.0% (n=100)
  - qwen3-8b-nothink/medqa/my professor: p_answer_changed=11.0% (n=100)
  - qwen3-8b-nothink/medqa/my rock: p_answer_changed=11.0% (n=100)
  - qwen3-8b-nothink/mmlu/a Stanford professor: p_answer_changed=27.0% (n=100)
  - qwen3-8b-nothink/mmlu/a fortune cookie: p_answer_changed=27.0% (n=100)
  - qwen3-8b-nothink/mmlu/a stranger on the bus: p_answer_changed=21.0% (n=100)
  - qwen3-8b-nothink/mmlu/my best friend: p_answer_changed=24.0% (n=100)
  - qwen3-8b-nothink/mmlu/my dog: p_answer_changed=19.0% (n=100)
  - qwen3-8b-nothink/mmlu/my horoscope: p_answer_changed=23.0% (n=100)
  - qwen3-8b-nothink/mmlu/my mom: p_answer_changed=24.0% (n=100)
  - qwen3-8b-nothink/mmlu/my professor: p_answer_changed=28.0% (n=100)
  - qwen3-8b-nothink/mmlu/my rock: p_answer_changed=23.0% (n=100)
  - qwen3-8b-think/agieval/a Stanford professor: p_answer_changed=51.9% (n=27)
  - qwen3-8b-think/agieval/a fortune cookie: p_answer_changed=48.1% (n=27)
  - qwen3-8b-think/agieval/a stranger on the bus: p_answer_changed=44.4% (n=27)
  - qwen3-8b-think/agieval/my best friend: p_answer_changed=51.9% (n=27)
  - qwen3-8b-think/agieval/my dog: p_answer_changed=40.7% (n=27)
  - qwen3-8b-think/agieval/my horoscope: p_answer_changed=55.6% (n=27)
  - qwen3-8b-think/agieval/my mom: p_answer_changed=59.3% (n=27)
  - qwen3-8b-think/agieval/my professor: p_answer_changed=55.6% (n=27)
  - qwen3-8b-think/agieval/my rock: p_answer_changed=29.6% (n=27)
  - qwen3-8b-think/medqa/a Stanford professor: p_answer_changed=14.7% (n=75)
  - qwen3-8b-think/medqa/a fortune cookie: p_answer_changed=14.7% (n=75)
  - qwen3-8b-think/medqa/a stranger on the bus: p_answer_changed=17.3% (n=75)
  - qwen3-8b-think/medqa/my best friend: p_answer_changed=22.7% (n=75)
  - qwen3-8b-think/medqa/my dog: p_answer_changed=17.3% (n=75)
  - qwen3-8b-think/medqa/my horoscope: p_answer_changed=20.0% (n=75)
  - qwen3-8b-think/medqa/my mom: p_answer_changed=20.0% (n=75)
  - qwen3-8b-think/medqa/my professor: p_answer_changed=10.7% (n=75)
  - qwen3-8b-think/medqa/my rock: p_answer_changed=17.3% (n=75)
  - r1-distill-qwen-7b/mmlu/a Stanford professor: p_answer_changed=18.0% (n=89)
  - r1-distill-qwen-7b/mmlu/a fortune cookie: p_answer_changed=20.2% (n=89)
  - r1-distill-qwen-7b/mmlu/a stranger on the bus: p_answer_changed=15.7% (n=89)
  - r1-distill-qwen-7b/mmlu/my best friend: p_answer_changed=15.7% (n=89)
  - r1-distill-qwen-7b/mmlu/my dog: p_answer_changed=20.2% (n=89)
  - r1-distill-qwen-7b/mmlu/my horoscope: p_answer_changed=20.2% (n=89)
  - r1-distill-qwen-7b/mmlu/my mom: p_answer_changed=20.2% (n=89)
  - r1-distill-qwen-7b/mmlu/my professor: p_answer_changed=11.2% (n=89)
  - r1-distill-qwen-7b/mmlu/my rock: p_answer_changed=12.4% (n=89)

## Effectiveness ordering & cross-model,dataset consistency

![Uptake heatmap](uptake_heatmap.png)

Sources ordered by mean P(uptake) across model,dataset cells (descending), used as heatmap column order: ['a Stanford professor', 'my professor', 'a fortune cookie', 'my rock', 'my horoscope', 'my mom', 'a stranger on the bus', 'my dog', 'my best friend']

Per-row tau vs mean ranking:

```
                       row  n_sources  tau_vs_mean_ranking
 olmo3-7b-instruct · medqa          9                0.611
  olmo3-7b-instruct · mmlu          9                0.229
    olmo3-7b-think · medqa          9                0.551
     olmo3-7b-think · mmlu          9                0.366
qwen3-8b-nothink · agieval          9                0.229
  qwen3-8b-nothink · medqa          9                0.177
   qwen3-8b-nothink · mmlu          9                0.400
  qwen3-8b-think · agieval          9                0.743
    qwen3-8b-think · medqa          9                0.761
     qwen3-8b-think · mmlu          9                0.589
 r1-distill-qwen-7b · mmlu          9                0.629
```


## Paired significance (McNemar, Holm-corrected within each model,dataset cell)

Full pairwise table: `analysis/uptake_pairwise.csv`. Highlights below: top-vs-bottom source per cell, and `a Stanford professor` vs every other source.

**olmo3-7b-instruct · medqa** (top source: a Stanford professor, bottom source: my mom)

```
            source_a              source_b  n_paired  b_a_only  c_b_only  p_value  p_holm
a Stanford professor                my mom       100        22         4   0.0005  0.0187
a Stanford professor                my dog       100        20         3   0.0005  0.0176
a Stanford professor        my best friend       100        18         4   0.0043  0.1390
a Stanford professor a stranger on the bus       100        16         4   0.0118  0.3664
a Stanford professor      a fortune cookie       100        18         7   0.0433  1.0000
a Stanford professor          my horoscope       100        18        10   0.1849  1.0000
a Stanford professor          my professor       100        10         9   1.0000  1.0000
a Stanford professor               my rock       100        17         7   0.0639  1.0000
```

**olmo3-7b-instruct · mmlu** (top source: a Stanford professor, bottom source: a fortune cookie)

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

**olmo3-7b-think · medqa** (top source: my professor, bottom source: my best friend)

```
            source_a              source_b  n_paired  b_a_only  c_b_only  p_value  p_holm
      my best friend          my professor        60         2        12   0.0129  0.4658
a Stanford professor      a fortune cookie        60         5         8   0.5811  1.0000
a Stanford professor a stranger on the bus        60         6         8   0.7905  1.0000
a Stanford professor        my best friend        60         6         2   0.2891  1.0000
a Stanford professor                my dog        60         4         3   1.0000  1.0000
a Stanford professor          my horoscope        60         6         6   1.0000  1.0000
a Stanford professor                my mom        60         3         5   0.7266  1.0000
a Stanford professor          my professor        60         6        12   0.2379  1.0000
a Stanford professor               my rock        60         2         5   0.4531  1.0000
```

**olmo3-7b-think · mmlu** (top source: a Stanford professor, bottom source: my horoscope)

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

**qwen3-8b-nothink · agieval** (top source: my professor, bottom source: a fortune cookie)

```
            source_a              source_b  n_paired  b_a_only  c_b_only  p_value  p_holm
    a fortune cookie          my professor        86        10        21   0.0708     1.0
a Stanford professor      a fortune cookie        86        13         7   0.2632     1.0
a Stanford professor a stranger on the bus        86        13        11   0.8388     1.0
a Stanford professor        my best friend        86         8         7   1.0000     1.0
a Stanford professor                my dog        86        11        10   1.0000     1.0
a Stanford professor          my horoscope        86         8        12   0.5034     1.0
a Stanford professor                my mom        86        10        11   1.0000     1.0
a Stanford professor          my professor        86        13        18   0.4731     1.0
a Stanford professor               my rock        86        11        11   1.0000     1.0
```

**qwen3-8b-nothink · medqa** (top source: my professor, bottom source: a fortune cookie)

```
            source_a              source_b  n_paired  b_a_only  c_b_only  p_value  p_holm
    a fortune cookie          my professor       100         3        12   0.0352     1.0
a Stanford professor      a fortune cookie       100         8         4   0.3877     1.0
a Stanford professor a stranger on the bus       100        12         8   0.5034     1.0
a Stanford professor        my best friend       100         9        10   1.0000     1.0
a Stanford professor                my dog       100         9         5   0.4240     1.0
a Stanford professor          my horoscope       100         6         9   0.6072     1.0
a Stanford professor                my mom       100         7         9   0.8036     1.0
a Stanford professor          my professor       100         6        11   0.3323     1.0
a Stanford professor               my rock       100         9        10   1.0000     1.0
```

**qwen3-8b-nothink · mmlu** (top source: my professor, bottom source: my rock)

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

**qwen3-8b-think · agieval** (top source: a Stanford professor, bottom source: my best friend)

```
            source_a              source_b  n_paired  b_a_only  c_b_only  p_value  p_holm
a Stanford professor        my best friend        27        10         2   0.0386  1.0000
a Stanford professor a stranger on the bus        27         7         0   0.0156  0.5625
a Stanford professor      a fortune cookie        27         5         3   0.7266  1.0000
a Stanford professor                my dog        27        10         4   0.1796  1.0000
a Stanford professor          my horoscope        27         7         4   0.5488  1.0000
a Stanford professor                my mom        27         9         3   0.1460  1.0000
a Stanford professor          my professor        27         8         3   0.2266  1.0000
a Stanford professor               my rock        27         6         3   0.5078  1.0000
```

**qwen3-8b-think · medqa** (top source: a Stanford professor, bottom source: my best friend)

```
            source_a              source_b  n_paired  b_a_only  c_b_only  p_value  p_holm
a Stanford professor        my best friend        75        25         4   0.0001  0.0037
a Stanford professor a stranger on the bus        75        21         3   0.0003  0.0094
a Stanford professor          my horoscope        75        21         3   0.0003  0.0094
a Stanford professor                my mom        75        19         3   0.0009  0.0274
a Stanford professor                my dog        75        20         5   0.0041  0.1223
a Stanford professor      a fortune cookie        75        14         8   0.2863  1.0000
a Stanford professor          my professor        75        17        12   0.4583  1.0000
a Stanford professor               my rock        75        18         8   0.0755  1.0000
```

**qwen3-8b-think · mmlu** (top source: a Stanford professor, bottom source: my best friend)

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

**r1-distill-qwen-7b · mmlu** (top source: my professor, bottom source: my best friend)

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
model              dataset source                                                                                                       
olmo3-7b-instruct  medqa   a Stanford professor      39.0       61.0            15.0              18.0           0.385             0.295
                           a fortune cookie          39.0       61.0            11.0              11.0           0.282             0.180
                           a stranger on the bus     39.0       61.0            13.0               8.0           0.333             0.131
                           my best friend            39.0       61.0            11.0               8.0           0.282             0.131
                           my dog                    39.0       61.0            10.0               6.0           0.256             0.098
                           my horoscope              39.0       61.0            15.0              10.0           0.385             0.164
                           my mom                    39.0       61.0             7.0               8.0           0.179             0.131
                           my professor              39.0       61.0            18.0              14.0           0.462             0.230
                           my rock                   39.0       61.0            15.0               8.0           0.385             0.131
                   mmlu    a Stanford professor      16.0       84.0             4.0              13.0           0.250             0.155
                           a fortune cookie          16.0       84.0             2.0               2.0           0.125             0.024
                           a stranger on the bus     16.0       84.0             3.0               1.0           0.188             0.012
                           my best friend            16.0       84.0             6.0               4.0           0.375             0.048
                           my dog                    16.0       84.0             5.0               1.0           0.312             0.012
                           my horoscope              16.0       84.0             5.0               3.0           0.312             0.036
                           my mom                    16.0       84.0             7.0               4.0           0.438             0.048
                           my professor              16.0       84.0             7.0               8.0           0.438             0.095
                           my rock                   16.0       84.0             4.0               2.0           0.250             0.024
olmo3-7b-think     medqa   a Stanford professor      33.0       27.0             2.0               5.0           0.061             0.185
                           a fortune cookie          33.0       27.0             6.0               4.0           0.182             0.148
                           a stranger on the bus     33.0       27.0             6.0               3.0           0.182             0.111
                           my best friend            33.0       27.0             2.0               1.0           0.061             0.037
                           my dog                    33.0       27.0             3.0               3.0           0.091             0.111
                           my horoscope              33.0       27.0             4.0               3.0           0.121             0.111
                           my mom                    33.0       27.0             5.0               4.0           0.152             0.148
                           my professor              33.0       27.0             6.0               7.0           0.182             0.259
                           my rock                   33.0       27.0             6.0               4.0           0.182             0.148
                   mmlu    a Stanford professor      18.0       75.0             5.0              15.0           0.278             0.200
                           a fortune cookie          18.0       75.0             6.0              12.0           0.333             0.160
                           a stranger on the bus     18.0       75.0             6.0               4.0           0.333             0.053
                           my best friend            18.0       75.0             6.0               6.0           0.333             0.080
                           my dog                    18.0       75.0             6.0               6.0           0.333             0.080
                           my horoscope              18.0       75.0             3.0               5.0           0.167             0.067
                           my mom                    18.0       75.0             7.0               6.0           0.389             0.080
                           my professor              18.0       75.0             5.0               6.0           0.278             0.080
                           my rock                   18.0       75.0             7.0               8.0           0.389             0.107
qwen3-8b-nothink   agieval a Stanford professor      47.0       39.0            17.0               7.0           0.362             0.179
                           a fortune cookie          47.0       39.0            12.0               6.0           0.255             0.154
                           a stranger on the bus     47.0       39.0            15.0               7.0           0.319             0.179
                           my best friend            47.0       39.0            19.0               4.0           0.404             0.103
                           my dog                    47.0       39.0            17.0               6.0           0.362             0.154
                           my horoscope              47.0       39.0            16.0              12.0           0.340             0.308
                           my mom                    47.0       39.0            15.0              10.0           0.319             0.256
                           my professor              47.0       39.0            21.0               8.0           0.447             0.205
                           my rock                   47.0       39.0            15.0               9.0           0.319             0.231
                   medqa   a Stanford professor      35.0       65.0             9.0               8.0           0.257             0.123
                           a fortune cookie          35.0       65.0             8.0               5.0           0.229             0.077
                           a stranger on the bus     35.0       65.0             6.0               7.0           0.171             0.108
                           my best friend            35.0       65.0            10.0               8.0           0.286             0.123
                           my dog                    35.0       65.0             5.0               8.0           0.143             0.123
                           my horoscope              35.0       65.0             9.0              11.0           0.257             0.169
                           my mom                    35.0       65.0             9.0              10.0           0.257             0.154
                           my professor              35.0       65.0             9.0              13.0           0.257             0.200
                           my rock                   35.0       65.0             8.0              10.0           0.229             0.154
                   mmlu    a Stanford professor      32.0       68.0             7.0               7.0           0.219             0.103
                           a fortune cookie          32.0       68.0             5.0               7.0           0.156             0.103
                           a stranger on the bus     32.0       68.0             6.0               7.0           0.188             0.103
                           my best friend            32.0       68.0             4.0               7.0           0.125             0.103
                           my dog                    32.0       68.0             5.0               5.0           0.156             0.074
                           my horoscope              32.0       68.0             5.0               8.0           0.156             0.118
                           my mom                    32.0       68.0             6.0               6.0           0.188             0.088
                           my professor              32.0       68.0             6.0               9.0           0.188             0.132
                           my rock                   32.0       68.0             4.0               5.0           0.125             0.074
qwen3-8b-think     agieval a Stanford professor      15.0       12.0             6.0               8.0           0.400             0.667
                           a fortune cookie          15.0       12.0             5.0               7.0           0.333             0.583
                           a stranger on the bus     15.0       12.0             3.0               4.0           0.200             0.333
                           my best friend            15.0       12.0             1.0               5.0           0.067             0.417
                           my dog                    15.0       12.0             5.0               3.0           0.333             0.250
                           my horoscope              15.0       12.0             7.0               4.0           0.467             0.333
                           my mom                    15.0       12.0             4.0               4.0           0.267             0.333
                           my professor              15.0       12.0             3.0               6.0           0.200             0.500
                           my rock                   15.0       12.0             5.0               6.0           0.333             0.500
                   medqa   a Stanford professor      16.0       59.0             5.0              24.0           0.312             0.407
                           a fortune cookie          16.0       59.0             6.0              17.0           0.375             0.288
                           a stranger on the bus     16.0       59.0             2.0               9.0           0.125             0.153
                           my best friend            16.0       59.0             0.0               8.0           0.000             0.136
                           my dog                    16.0       59.0             3.0              11.0           0.188             0.186
                           my horoscope              16.0       59.0             3.0               8.0           0.188             0.136
                           my mom                    16.0       59.0             4.0               9.0           0.250             0.153
                           my professor              16.0       59.0             4.0              20.0           0.250             0.339
                           my rock                   16.0       59.0             5.0              14.0           0.312             0.237
                   mmlu    a Stanford professor       6.0       89.0             2.0              14.0           0.333             0.157
                           a fortune cookie           6.0       89.0             2.0               2.0           0.333             0.022
                           a stranger on the bus      6.0       89.0             1.0               5.0           0.167             0.056
                           my best friend             6.0       89.0             1.0               2.0           0.167             0.022
                           my dog                     6.0       89.0             1.0               2.0           0.167             0.022
                           my horoscope               6.0       89.0             2.0               4.0           0.333             0.045
                           my mom                     6.0       89.0             3.0               4.0           0.500             0.045
                           my professor               6.0       89.0             2.0              11.0           0.333             0.124
                           my rock                    6.0       89.0             1.0               5.0           0.167             0.056
r1-distill-qwen-7b mmlu    a Stanford professor      17.0       72.0             4.0               4.0           0.235             0.056
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

  - olmo3-7b-instruct/mmlu/my best friend: 4/10 uptakes (40%) come from hint_is_gold rows, which are only 5% of that cell's data.
  - olmo3-7b-instruct/mmlu/my mom: 3/11 uptakes (27%) come from hint_is_gold rows, which are only 5% of that cell's data.
  - olmo3-7b-instruct/mmlu/my professor: 4/15 uptakes (27%) come from hint_is_gold rows, which are only 5% of that cell's data.
  - olmo3-7b-think/mmlu/a Stanford professor: 3/20 uptakes (15%) come from hint_is_gold rows, which are only 6% of that cell's data.
  - olmo3-7b-think/mmlu/a fortune cookie: 4/18 uptakes (22%) come from hint_is_gold rows, which are only 6% of that cell's data.
  - olmo3-7b-think/mmlu/a stranger on the bus: 5/10 uptakes (50%) come from hint_is_gold rows, which are only 6% of that cell's data.
  - olmo3-7b-think/mmlu/my best friend: 4/12 uptakes (33%) come from hint_is_gold rows, which are only 6% of that cell's data.
  - olmo3-7b-think/mmlu/my dog: 3/12 uptakes (25%) come from hint_is_gold rows, which are only 6% of that cell's data.
  - olmo3-7b-think/mmlu/my mom: 4/13 uptakes (31%) come from hint_is_gold rows, which are only 6% of that cell's data.
  - olmo3-7b-think/mmlu/my professor: 4/11 uptakes (36%) come from hint_is_gold rows, which are only 6% of that cell's data.
  - olmo3-7b-think/mmlu/my rock: 4/15 uptakes (27%) come from hint_is_gold rows, which are only 6% of that cell's data.
  - qwen3-8b-nothink/mmlu/a Stanford professor: 3/14 uptakes (21%) come from hint_is_gold rows, which are only 9% of that cell's data.
  - qwen3-8b-nothink/mmlu/a fortune cookie: 3/12 uptakes (25%) come from hint_is_gold rows, which are only 9% of that cell's data.
  - qwen3-8b-nothink/mmlu/a stranger on the bus: 4/13 uptakes (31%) come from hint_is_gold rows, which are only 9% of that cell's data.
  - qwen3-8b-nothink/mmlu/my best friend: 3/11 uptakes (27%) come from hint_is_gold rows, which are only 9% of that cell's data.
  - qwen3-8b-nothink/mmlu/my dog: 5/10 uptakes (50%) come from hint_is_gold rows, which are only 9% of that cell's data.
  - qwen3-8b-nothink/mmlu/my horoscope: 3/13 uptakes (23%) come from hint_is_gold rows, which are only 9% of that cell's data.
  - qwen3-8b-nothink/mmlu/my mom: 4/12 uptakes (33%) come from hint_is_gold rows, which are only 9% of that cell's data.
  - qwen3-8b-nothink/mmlu/my professor: 4/15 uptakes (27%) come from hint_is_gold rows, which are only 9% of that cell's data.
  - qwen3-8b-nothink/mmlu/my rock: 4/9 uptakes (44%) come from hint_is_gold rows, which are only 9% of that cell's data.
  - r1-distill-qwen-7b/mmlu/a fortune cookie: 3/10 uptakes (30%) come from hint_is_gold rows, which are only 4% of that cell's data.
  - r1-distill-qwen-7b/mmlu/my dog: 3/6 uptakes (50%) come from hint_is_gold rows, which are only 4% of that cell's data.

## Caveats

- All proportions above are reported with denominator `n`; treat any cell with small `n_uptake` (a handful of flips out of 100) as noisy, especially in the McNemar tests.
- `results/*.summary.json` and `results/sweep_summaries.json` were treated as informative, not authoritative; all numbers in this report are recomputed from the raw `.jsonl` records.
- This is an aggregate report spanning multiple datasets; every table above groups by (model, dataset, source), so a source name reused across datasets is never pooled. Run with `--dataset <name>` for a report scoped to just one dataset.
