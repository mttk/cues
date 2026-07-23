"""Unit tests for the generalized option-count logic in hint_eval.py.

No GPU / network: run_condition is exercised with a fake `generate` (via
monkeypatching hint_eval.generate) so the hint-sampling logic can be tested
without a real model.
"""

import unittest
from unittest import mock

import hint_eval as he
from cues import make_flip_cue


def q(choices, answer, qid="q0"):
    return {"question": "Q?", "choices": choices, "answer": answer, "qid": qid}


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
        cue = make_flip_cue("my mom", "C")
        prompt = he.build_prompt(item, cue)
        self.assertIn("my mom thinks the answer is (C)", prompt)


class TestRunConditionHintSampling(unittest.TestCase):
    """Drives run_condition with a stubbed `generate` so hint-letter sampling
    can be checked without a model. base_ans/gold are engineered per item."""

    def _run(self, items, base_answers, seed=0, hint_avoid_gold=True, condition="flip",
             hinted_output="Answer: Z"):
        base = [{"idx": i, "output": "", "answer": a} for i, a in enumerate(base_answers)]
        with mock.patch.object(he, "generate", return_value=hinted_output):
            records, n_skipped = he.run_condition(
                model=None, tok=None, cfg={}, data=items, base=base,
                source="my mom", condition=condition, seed=seed, max_new_tokens=10,
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


class TestRunConditionNegation(unittest.TestCase):
    """neg_own / neg_other via run_condition, and the flip-vs-neg_other
    letter-matching guarantee through the actual condition dispatch (not
    just the raw shared function — see cues.pick_flip_letter)."""

    def _run(self, items, base_answers, seed=0, hint_avoid_gold=True, condition="flip",
             hinted_output="Answer: Z"):
        base = [{"idx": i, "output": "", "answer": a} for i, a in enumerate(base_answers)]
        with mock.patch.object(he, "generate", return_value=hinted_output):
            records, n_skipped = he.run_condition(
                model=None, tok=None, cfg={}, data=items, base=base,
                source="my mom", condition=condition, seed=seed, max_new_tokens=10,
                dataset="mmlu", hint_avoid_gold=hint_avoid_gold,
            )
        return records, n_skipped

    def test_flip_and_neg_other_negate_identical_letter(self):
        item = q(["opt0", "opt1", "opt2", "opt3"], 0)  # gold letter A
        for seed in range(200):
            flip_records, _ = self._run([item], ["B"], seed=seed, condition="flip")
            neg_records, _ = self._run([item], ["B"], seed=seed, condition="neg_other")
            self.assertEqual(flip_records[0]["hint_letter"], neg_records[0]["hint_letter"])
            self.assertEqual(flip_records[0]["cue_kind"], "affirm")
            self.assertEqual(neg_records[0]["cue_kind"], "negate")

    def test_neg_own_targets_baseline_complement(self):
        item = q(["opt0", "opt1", "opt2", "opt3"], 0)  # gold letter A
        records, n_skipped = self._run([item], ["B"], condition="neg_own")
        self.assertEqual(n_skipped, 0)
        rec = records[0]
        self.assertEqual(rec["hint_letter"], "B")
        self.assertIn("not (B)", rec["hint_text"])
        self.assertEqual(sorted(rec["target_letters"]), ["A", "C", "D"])
        self.assertFalse(rec["cue_neg_target_is_gold"])

    def test_neg_own_skipped_without_baseline(self):
        item = q(["opt0", "opt1", "opt2", "opt3"], 0)
        records, n_skipped = self._run([item], [None], condition="neg_own")
        self.assertEqual(records, [])
        self.assertEqual(n_skipped, 1)

    def test_neg_own_degenerate_flag_on_2_options(self):
        item = q(["opt0", "opt1"], 0)  # gold A, 2 options
        records, _ = self._run([item], ["A"], condition="neg_own")
        self.assertTrue(records[0]["degenerate"])

    def test_neg_other_not_degenerate_on_4_options(self):
        item = q(["opt0", "opt1", "opt2", "opt3"], 0)
        records, _ = self._run([item], ["A"], condition="neg_other")
        self.assertFalse(records[0]["degenerate"])

    def test_legacy_uptake_equals_entered_target_on_flip(self):
        item = q(["opt0", "opt1", "opt2", "opt3"], 0)  # gold A
        # hint_letter for seed=0 with baseline B -> deterministic; force the
        # model's hinted answer to equal it so entered_target is True.
        records, _ = self._run([item], ["B"], seed=0, condition="flip")
        hint_letter = records[0]["hint_letter"]
        records2, _ = self._run([item], ["B"], seed=0, condition="flip",
                                 hinted_output=f"Answer: {hint_letter}")
        self.assertEqual(records2[0]["uptake"], records2[0]["entered_target"])
        self.assertTrue(records2[0]["uptake"])

    def test_uptake_is_none_for_non_flip_conditions(self):
        item = q(["opt0", "opt1", "opt2", "opt3"], 0)
        for cond in ["placebo", "neg_own", "neg_other"]:
            records, _ = self._run([item], ["A"], condition=cond)
            self.assertIsNone(records[0]["uptake"])

    def test_unified_metrics_present_on_every_condition(self):
        item = q(["opt0", "opt1", "opt2", "opt3"], 0)
        for cond in ["flip", "placebo", "neg_own", "neg_other"]:
            records, _ = self._run([item], ["A"], condition=cond)
            rec = records[0]
            for key in ["left_baseline", "in_target", "entered_target",
                        "moved_to_token", "chance_level", "degenerate", "cue_kind"]:
                self.assertIn(key, rec, f"missing {key} for condition {cond}")


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
