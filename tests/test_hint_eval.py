"""Unit tests for the generalized option-count logic in hint_eval.py.

No GPU / network: run_condition is exercised with a fake `generate` (via
monkeypatching hint_eval.generate) so the hint-sampling logic can be tested
without a real model.
"""

import unittest
from unittest import mock

import hint_eval as he


def q(choices, answer):
    return {"question": "Q?", "choices": choices, "answer": answer}


class TestLetters(unittest.TestCase):
    def test_four_options(self):
        self.assertEqual(he.letters(q(["a", "b", "c", "d"], 0)), "ABCD")

    def test_ten_options(self):
        self.assertEqual(he.letters(q(list("abcdefghij"), 0)), "ABCDEFGHIJ")

    def test_two_options(self):
        self.assertEqual(he.letters(q(["a", "b"], 0)), "AB")


class TestExtractAnswer(unittest.TestCase):
    def test_answer_line_last_match_wins(self):
        text = "Answer: B\nWait, actually Answer: C"
        self.assertEqual(he.extract_answer(text, 4), "C")

    def test_ten_option_j_accepted(self):
        self.assertEqual(he.extract_answer("Answer: J", 10), "J")

    def test_ten_option_j_rejected_for_four_option_question(self):
        self.assertIsNone(he.extract_answer("Answer: J", 4))

    def test_parenthesised_fallback(self):
        self.assertEqual(he.extract_answer("I think it's (C) because...", 4), "C")

    def test_parenthesised_fallback_out_of_range_rejected(self):
        self.assertIsNone(he.extract_answer("I think it's (F) because...", 4))

    def test_no_match_returns_none(self):
        self.assertIsNone(he.extract_answer("no letter here", 4))

    def test_two_option_range(self):
        self.assertEqual(he.extract_answer("Answer: B", 2), "B")
        self.assertIsNone(he.extract_answer("Answer: C", 2))


class TestBuildPrompt(unittest.TestCase):
    def test_unhinted_has_no_hint_text(self):
        item = q(["x", "y"], 0)
        prompt = he.build_prompt(item)
        self.assertNotIn("thinks the answer is", prompt)
        self.assertIn("(A) x", prompt)
        self.assertIn("(B) y", prompt)

    def test_hinted_includes_source_and_letter(self):
        item = q(["x", "y", "z"], 0)
        prompt = he.build_prompt(item, hint_source="my mom", hint_letter="C")
        self.assertIn("my mom thinks the answer is (C)", prompt)


class TestRunConditionHintSampling(unittest.TestCase):
    """Drives run_condition with a stubbed `generate` so hint-letter sampling
    can be checked without a model. base_ans/gold are engineered per item."""

    def _run(self, items, base_answers, seed=0, hint_avoid_gold=True, n_trials=1):
        base = [{"idx": i, "output": "", "answer": a} for i, a in enumerate(base_answers)]
        with mock.patch.object(he, "generate", return_value="Answer: Z"):
            records, n_skipped = he.run_condition(
                model=None, tok=None, cfg={}, data=items, base=base,
                source="my mom", condition="flip", seed=seed, max_new_tokens=10,
                dataset="mmlu", hint_avoid_gold=hint_avoid_gold,
            )
        return records, n_skipped

    def test_hint_never_equals_gold_or_baseline_with_flag_on(self):
        # 4-option item, baseline wrong (B), gold is A -> with hint_avoid_gold,
        # hint must be drawn from {C, D} across many seeds.
        item = q(["opt0", "opt1", "opt2", "opt3"], 0)  # gold letter A
        seen_letters = set()
        for seed in range(200):
            records, _ = self._run([item], ["B"], seed=seed, hint_avoid_gold=True)
            self.assertEqual(len(records), 1)
            rec = records[0]
            self.assertNotEqual(rec["hint_letter"], "A")  # gold
            self.assertNotEqual(rec["hint_letter"], "B")  # baseline
            seen_letters.add(rec["hint_letter"])
        self.assertEqual(seen_letters, {"C", "D"})

    def test_hint_is_gold_always_recorded_even_with_flag_off(self):
        item = q(["opt0", "opt1", "opt2", "opt3"], 0)  # gold letter A
        records, _ = self._run([item], ["B"], seed=1, hint_avoid_gold=False)
        self.assertIn("hint_is_gold", records[0])

    def test_flag_off_can_hint_toward_gold(self):
        # With the flag off, only baseline (B) is avoided, so gold (A) is a
        # legal hint target across many seeds.
        item = q(["opt0", "opt1", "opt2", "opt3"], 0)
        saw_gold_hint = False
        for seed in range(200):
            records, _ = self._run([item], ["B"], seed=seed, hint_avoid_gold=False)
            if records[0]["hint_letter"] == "A":
                saw_gold_hint = True
                break
        self.assertTrue(saw_gold_hint)

    def test_two_option_skip_path(self):
        # 2 options, baseline wrong (B), gold A -> avoid-set {A, B} = both
        # options -> item must be skipped and counted.
        item = q(["opt0", "opt1"], 0)  # gold letter A
        records, n_skipped = self._run([item], ["B"], seed=0, hint_avoid_gold=True)
        self.assertEqual(records, [])
        self.assertEqual(n_skipped, 1)

    def test_two_option_no_skip_when_baseline_correct(self):
        # baseline == gold == A -> avoid-set collapses to {A}, hint = B, fine.
        item = q(["opt0", "opt1"], 0)
        records, n_skipped = self._run([item], ["A"], seed=0, hint_avoid_gold=True)
        self.assertEqual(n_skipped, 0)
        self.assertEqual(records[0]["hint_letter"], "B")


class TestFilterByLength(unittest.TestCase):
    def test_drops_long_questions(self):
        items = [{"question": "short"}, {"question": "x" * 100}]
        kept, n_skipped = he.filter_by_length(items, max_chars=50)
        self.assertEqual(len(kept), 1)
        self.assertEqual(n_skipped, 1)


class TestResultTagBackwardCompat(unittest.TestCase):
    def test_mmlu_tag_unchanged_shape(self):
        tag = he.result_tag("olmo3-7b-instruct", "my mom", "mmlu", "high_school_psychology", "flip")
        self.assertEqual(tag, "olmo3-7b-instruct__my_mom__high_school_psychology__flip")

    def test_non_mmlu_tag_includes_dataset(self):
        tag = he.result_tag("olmo3-7b-instruct", "my mom", "medqa", None, "flip")
        self.assertEqual(tag, "olmo3-7b-instruct__my_mom__medqa__all__flip")

    def test_agieval_tag_includes_subset(self):
        tag = he.result_tag("olmo3-7b-instruct", "my mom", "agieval", "lsat-lr", "flip")
        self.assertEqual(tag, "olmo3-7b-instruct__my_mom__agieval__lsat-lr__flip")


class TestBaselineCachePaths(unittest.TestCase):
    def test_new_format(self):
        p = he.baseline_cache_path("results", "olmo3-7b-instruct", "medqa", None, 100, 0)
        self.assertEqual(p.name, "olmo3-7b-instruct__medqa__all__n100__s0.jsonl")

    def test_legacy_mmlu_format_matches_old_convention(self):
        p = he.legacy_mmlu_baseline_cache_path("results", "olmo3-7b-instruct", "high_school_psychology", 100)
        self.assertEqual(p.name, "olmo3-7b-instruct__high_school_psychology__n100.jsonl")


if __name__ == "__main__":
    unittest.main()
