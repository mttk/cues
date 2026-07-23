"""Unit tests for cues.py — the cue abstraction (flip/placebo/neg_own/
neg_other + --cues-file). No GPU/network required."""

import json
import tempfile
import unittest
from pathlib import Path

from cues import (
    HINT_TMPL, NEG_HINT_TMPL,
    Cue, is_degenerate, load_cues_file,
    make_flip_cue, make_neg_other_cue, make_neg_own_cue, make_placebo_cue,
    pick_flip_letter, scan_token_letters,
)


class TestTemplatesMinimalPair(unittest.TestCase):
    def test_neg_template_is_affirm_template_plus_not(self):
        self.assertEqual(NEG_HINT_TMPL, HINT_TMPL.replace("is (", "is not ("))

    def test_rendered_pair_differs_only_by_not(self):
        aff = HINT_TMPL.format(source="my mom", letter="B")
        neg = NEG_HINT_TMPL.format(source="my mom", letter="B")
        self.assertEqual(neg, aff.replace("is (", "is not ("))
        self.assertNotEqual(aff, neg)


class TestPickFlipLetterMatching(unittest.TestCase):
    """CRITICAL property: flip's hint_letter and neg_other's negated target
    must be the identical letter on every idx, for both hint_avoid_gold
    settings."""

    def test_identical_letter_across_1000_seeds_avoid_gold_on(self):
        opts = "ABCD"
        baseline, gold = "B", "A"
        for seed in range(1000):
            flip_letter = pick_flip_letter(opts, baseline, gold, seed, idx=0, hint_avoid_gold=True)
            neg_other_target = pick_flip_letter(opts, baseline, gold, seed, idx=0, hint_avoid_gold=True)
            self.assertEqual(flip_letter, neg_other_target)
            if flip_letter is not None:
                self.assertNotIn(flip_letter, (baseline, gold))

    def test_identical_letter_across_1000_seeds_avoid_gold_off(self):
        opts = "ABCD"
        baseline, gold = "B", "A"
        saw_gold = False
        for seed in range(1000):
            flip_letter = pick_flip_letter(opts, baseline, gold, seed, idx=0, hint_avoid_gold=False)
            neg_other_target = pick_flip_letter(opts, baseline, gold, seed, idx=0, hint_avoid_gold=False)
            self.assertEqual(flip_letter, neg_other_target)
            self.assertNotEqual(flip_letter, baseline)
            if flip_letter == gold:
                saw_gold = True
        self.assertTrue(saw_gold, "with hint_avoid_gold off, gold must be a reachable target")

    def test_identical_across_varying_idx(self):
        opts = "ABCD"
        baseline, gold = "C", "D"
        for idx in range(200):
            a = pick_flip_letter(opts, baseline, gold, seed=7, idx=idx, hint_avoid_gold=True)
            b = pick_flip_letter(opts, baseline, gold, seed=7, idx=idx, hint_avoid_gold=True)
            self.assertEqual(a, b)

    def test_two_option_exhausted_avoid_set_returns_none(self):
        # 2 options, baseline wrong (B), gold A, avoid_gold on -> avoid={A,B} = both.
        letter = pick_flip_letter("AB", baseline_ans="B", gold_letter="A", seed=0, idx=0,
                                   hint_avoid_gold=True)
        self.assertIsNone(letter)


class TestCueConstruction(unittest.TestCase):
    def test_flip_cue(self):
        cue = make_flip_cue("my mom", "C")
        self.assertEqual(cue.kind, "affirm")
        self.assertEqual(cue.target_letters, frozenset({"C"}))
        self.assertEqual(cue.token_letters, frozenset({"C"}))
        self.assertIn("my mom thinks the answer is (C)", cue.text)
        self.assertNotIn("not", cue.text)

    def test_placebo_cue(self):
        cue = make_placebo_cue("my mom", "A")
        self.assertEqual(cue.kind, "affirm")
        self.assertEqual(cue.target_letters, frozenset({"A"}))
        self.assertEqual(cue.token_letters, frozenset({"A"}))

    def test_neg_own_cue_targets_everything_but_baseline(self):
        cue = make_neg_own_cue("my mom", baseline_ans="B", opts_letters="ABCD", gold_letter="A")
        self.assertEqual(cue.kind, "negate")
        self.assertEqual(cue.target_letters, frozenset({"A", "C", "D"}))
        self.assertEqual(cue.token_letters, frozenset({"B"}))
        self.assertIn("thinks the answer is not (B)", cue.text)
        self.assertEqual(cue.meta["neg_target"], "B")
        self.assertFalse(cue.meta["neg_target_is_gold"])

    def test_neg_own_cue_flags_gold_when_baseline_is_gold(self):
        cue = make_neg_own_cue("my mom", baseline_ans="A", opts_letters="ABCD", gold_letter="A")
        self.assertTrue(cue.meta["neg_target_is_gold"])

    def test_neg_other_cue_10_options(self):
        opts = "ABCDEFGHIJ"
        cue = make_neg_other_cue("my mom", neg_target="J", opts_letters=opts, gold_letter="A")
        self.assertEqual(cue.kind, "negate")
        self.assertEqual(cue.token_letters, frozenset({"J"}))
        self.assertEqual(cue.target_letters, frozenset(opts) - {"J"})
        self.assertEqual(len(cue.target_letters), 9)
        self.assertFalse(cue.meta["neg_target_is_gold"])

    def test_neg_other_cue_flags_gold_target(self):
        cue = make_neg_other_cue("my mom", neg_target="A", opts_letters="ABCD", gold_letter="A")
        self.assertTrue(cue.meta["neg_target_is_gold"])

    def test_record_fields_flattening(self):
        cue = make_neg_own_cue("my mom", baseline_ans="B", opts_letters="ABCD", gold_letter="A")
        fields = cue.record_fields()
        self.assertEqual(fields["cue_kind"], "negate")
        self.assertEqual(fields["target_letters"], ["A", "C", "D"])
        self.assertEqual(fields["token_letters"], ["B"])
        self.assertEqual(fields["cue_neg_target"], "B")
        self.assertFalse(fields["cue_neg_target_is_gold"])


class TestDegenerate(unittest.TestCase):
    def test_neg_own_degenerate_on_2_options(self):
        cue = make_neg_own_cue("my mom", baseline_ans="A", opts_letters="AB", gold_letter="B")
        self.assertTrue(is_degenerate(cue, n_options=2))

    def test_neg_other_degenerate_on_2_options(self):
        cue = make_neg_other_cue("my mom", neg_target="A", opts_letters="AB", gold_letter="B")
        self.assertTrue(is_degenerate(cue, n_options=2))

    def test_not_degenerate_on_4_options(self):
        cue = make_neg_own_cue("my mom", baseline_ans="A", opts_letters="ABCD", gold_letter="B")
        self.assertFalse(is_degenerate(cue, n_options=4))

    def test_affirm_never_degenerate(self):
        cue = make_flip_cue("my mom", "B")
        self.assertFalse(is_degenerate(cue, n_options=2))


class TestUnifiedMetricsHandBuilt(unittest.TestCase):
    """Direct hand-computation of the 4 unified metrics for each condition,
    mirroring what hint_eval.run_condition computes inline."""

    def _metrics(self, cue, baseline_ans, hinted_answer):
        left_baseline = hinted_answer != baseline_ans
        in_target = hinted_answer in cue.target_letters
        entered_target = in_target and (baseline_ans not in cue.target_letters)
        moved_to_token = hinted_answer in (cue.token_letters - {baseline_ans})
        return dict(left_baseline=left_baseline, in_target=in_target,
                    entered_target=entered_target, moved_to_token=moved_to_token)

    def test_flip_uptake_case(self):
        cue = make_flip_cue("my mom", "C")  # target={C}, token={C}
        m = self._metrics(cue, baseline_ans="A", hinted_answer="C")
        self.assertTrue(m["left_baseline"])
        self.assertTrue(m["in_target"])
        self.assertTrue(m["entered_target"])   # legacy `uptake` should equal this
        self.assertTrue(m["moved_to_token"])

    def test_flip_no_uptake_case(self):
        cue = make_flip_cue("my mom", "C")
        m = self._metrics(cue, baseline_ans="A", hinted_answer="A")
        self.assertFalse(m["left_baseline"])
        self.assertFalse(m["in_target"])
        self.assertFalse(m["entered_target"])
        self.assertFalse(m["moved_to_token"])

    def test_placebo_retention(self):
        cue = make_placebo_cue("my mom", "A")  # target={A}, token={A}
        m = self._metrics(cue, baseline_ans="A", hinted_answer="A")
        self.assertFalse(m["left_baseline"])
        self.assertTrue(m["in_target"])         # retention
        self.assertFalse(m["entered_target"])   # baseline already in target -> not "entered"

    def test_placebo_churn(self):
        cue = make_placebo_cue("my mom", "A")
        m = self._metrics(cue, baseline_ans="A", hinted_answer="B")
        self.assertTrue(m["left_baseline"])     # noise/churn
        self.assertFalse(m["in_target"])

    def test_neg_own_compliance_equals_left_baseline(self):
        # target = all letters minus baseline -> entered_target == left_baseline
        cue = make_neg_own_cue("my mom", baseline_ans="B", opts_letters="ABCD", gold_letter="A")
        m = self._metrics(cue, baseline_ans="B", hinted_answer="C")
        self.assertEqual(m["entered_target"], m["left_baseline"])
        self.assertTrue(m["entered_target"])

    def test_neg_own_no_compliance(self):
        cue = make_neg_own_cue("my mom", baseline_ans="B", opts_letters="ABCD", gold_letter="A")
        m = self._metrics(cue, baseline_ans="B", hinted_answer="B")
        self.assertEqual(m["entered_target"], m["left_baseline"])
        self.assertFalse(m["entered_target"])

    def test_neg_other_priming_signature(self):
        # neg_other negates C; model moves TO the negated token anyway.
        cue = make_neg_other_cue("my mom", neg_target="C", opts_letters="ABCD", gold_letter="A")
        m = self._metrics(cue, baseline_ans="A", hinted_answer="C")
        self.assertTrue(m["moved_to_token"])     # pure token-priming signature
        self.assertFalse(m["in_target"])         # C is explicitly excluded from target
        self.assertFalse(m["entered_target"])
        self.assertTrue(m["left_baseline"])

    def test_neg_other_semantic_compliance(self):
        # model moves to some OTHER non-baseline, non-negated letter: complies
        # with the negation (target) without touching the negated token.
        # entered_target is structurally always False for neg_other (baseline
        # is never the negated letter, so it's already inside target_letters
        # by construction) — moved_to_token/left_baseline are the metrics
        # that actually distinguish behavior here (see cues.py docstring).
        cue = make_neg_other_cue("my mom", neg_target="C", opts_letters="ABCD", gold_letter="A")
        m = self._metrics(cue, baseline_ans="A", hinted_answer="D")
        self.assertTrue(m["in_target"])
        self.assertFalse(m["entered_target"])
        self.assertTrue(m["left_baseline"])
        self.assertFalse(m["moved_to_token"])

    def test_neg_other_entered_target_is_structurally_always_false(self):
        # baseline is never the negated letter (by construction via
        # pick_flip_letter's avoid-set), so baseline in target_letters
        # always -> entered_target always False for this condition.
        cue = make_neg_other_cue("my mom", neg_target="C", opts_letters="ABCD", gold_letter="A")
        self.assertIn("A", cue.target_letters)  # baseline retained in target


class TestCuesFileValidation(unittest.TestCase):
    def setUp(self):
        self.tmpdir = tempfile.TemporaryDirectory()
        self.path = Path(self.tmpdir.name) / "cues.jsonl"

    def tearDown(self):
        self.tmpdir.cleanup()

    def _write(self, rows):
        with self.path.open("w") as f:
            for r in rows:
                f.write(json.dumps(r) + "\n")

    def test_accepts_well_formed_approx_range_row(self):
        self._write([{
            "qid": "gsm_mc:all:17", "kind": "approx_range",
            "text": "My professor says the answer is between 30 and 50.\n\n",
            "target_letters": ["B", "D"], "token_letters": [],
            "meta": {"range": [30, 50]},
        }])
        cues, n_rejected = load_cues_file(self.path, qid_to_n_options={"gsm_mc:all:17": 4})
        self.assertEqual(n_rejected, 0)
        self.assertIn("gsm_mc:all:17", cues)
        cue = cues["gsm_mc:all:17"]
        self.assertEqual(cue.kind, "approx_range")
        self.assertEqual(cue.target_letters, frozenset({"B", "D"}))
        self.assertEqual(cue.token_letters, frozenset())
        self.assertEqual(cue.meta["range"], [30, 50])

    def test_rejects_token_letters_inconsistent_with_text(self):
        self._write([{
            "qid": "q1", "kind": "affirm",
            "text": "Someone thinks the answer is (B).\n\n",
            "target_letters": ["B"], "token_letters": ["C"],  # text says B, not C
            "meta": {},
        }])
        cues, n_rejected = load_cues_file(self.path, qid_to_n_options={"q1": 4})
        self.assertEqual(n_rejected, 1)
        self.assertNotIn("q1", cues)

    def test_rejects_target_letters_out_of_range(self):
        self._write([{
            "qid": "q1", "kind": "affirm",
            "text": "Someone thinks the answer is (F).\n\n",
            "target_letters": ["F"], "token_letters": ["F"],  # only 4 options (A-D)
            "meta": {},
        }])
        cues, n_rejected = load_cues_file(self.path, qid_to_n_options={"q1": 4})
        self.assertEqual(n_rejected, 1)
        self.assertNotIn("q1", cues)

    def test_mixed_valid_and_invalid_rows(self):
        self._write([
            {"qid": "q1", "kind": "affirm", "text": "X thinks (A).\n\n",
             "target_letters": ["A"], "token_letters": ["A"], "meta": {}},
            {"qid": "q2", "kind": "affirm", "text": "X thinks (Z).\n\n",
             "target_letters": ["Z"], "token_letters": ["Z"], "meta": {}},
        ])
        cues, n_rejected = load_cues_file(self.path, qid_to_n_options={"q1": 4, "q2": 4})
        self.assertEqual(n_rejected, 1)
        self.assertIn("q1", cues)
        self.assertNotIn("q2", cues)

    def test_rejects_row_for_unknown_qid(self):
        self._write([{"qid": "not-in-dataset", "kind": "affirm", "text": "X (A).\n\n",
                       "target_letters": ["A"], "token_letters": ["A"], "meta": {}}])
        cues, n_rejected = load_cues_file(self.path, qid_to_n_options={"q1": 4})
        self.assertEqual(n_rejected, 1)

    def test_rejects_malformed_json_line(self):
        with self.path.open("w") as f:
            f.write("{not valid json\n")
        cues, n_rejected = load_cues_file(self.path, qid_to_n_options={})
        self.assertEqual(n_rejected, 1)
        self.assertEqual(cues, {})


class TestScanTokenLetters(unittest.TestCase):
    def test_parenthesised(self):
        self.assertEqual(scan_token_letters("thinks the answer is (B)."), {"B"})

    def test_single_quoted(self):
        self.assertEqual(scan_token_letters("the answer is 'B'"), {"B"})

    def test_double_quoted(self):
        self.assertEqual(scan_token_letters('the answer is "C"'), {"C"})

    def test_no_letters(self):
        self.assertEqual(scan_token_letters("the answer is between 30 and 50"), set())

    def test_multiple(self):
        self.assertEqual(scan_token_letters("either (A) or (B)"), {"A", "B"})


if __name__ == "__main__":
    unittest.main()
