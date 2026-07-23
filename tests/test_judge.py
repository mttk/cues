"""Unit tests for judge.py's cue_kind-aware rubric switching.

No network: the OpenAI client is mocked. Verifies that affirm-kind cues
(flip/placebo, including legacy pre-cue-abstraction records lacking a
`cue_kind` field) keep the original 3-label schema unchanged, while
negate-kind cues (neg_own/neg_other) get the extended rubric and the new
`contradicts_cue` label.
"""

import json
import unittest
from unittest import mock

import judge


def make_client(response_json):
    client = mock.MagicMock()
    resp = mock.MagicMock()
    resp.choices = [mock.MagicMock(message=mock.MagicMock(content=json.dumps(response_json)))]
    client.chat.completions.create.return_value = resp
    return client


class TestJudgeTextSchema(unittest.TestCase):
    def test_affirm_response_has_no_contradicts_cue(self):
        client = make_client({"mentions_hint": True, "acknowledges_influence": True,
                              "dismisses_hint": False, "evidence": "x"})
        out = judge.judge_text(client, "gpt-4o-mini", "hint", "answer text", "some output",
                                cue_kind="affirm")
        self.assertNotIn("contradicts_cue", out)
        self.assertFalse(out["empty_channel"])

    def test_negate_response_includes_contradicts_cue(self):
        client = make_client({"mentions_hint": True, "acknowledges_influence": True,
                              "dismisses_hint": False, "contradicts_cue": True, "evidence": "y"})
        out = judge.judge_text(client, "gpt-4o-mini", "hint", "answer text", "some output",
                                cue_kind="negate")
        self.assertTrue(out["contradicts_cue"])

    def test_empty_channel_negate_defaults_contradicts_cue_false(self):
        client = make_client({})  # unused: empty text short-circuits before any API call
        out = judge.judge_text(client, "gpt-4o-mini", "hint", "answer text", "   ",
                                cue_kind="negate")
        self.assertTrue(out["empty_channel"])
        self.assertFalse(out["contradicts_cue"])
        client.chat.completions.create.assert_not_called()

    def test_empty_channel_affirm_has_no_contradicts_cue(self):
        client = make_client({})
        out = judge.judge_text(client, "gpt-4o-mini", "hint", "answer text", "",
                                cue_kind="affirm")
        self.assertNotIn("contradicts_cue", out)

    def test_uses_negate_template_when_negate(self):
        client = make_client({"mentions_hint": False, "acknowledges_influence": False,
                              "dismisses_hint": False, "contradicts_cue": False, "evidence": ""})
        judge.judge_text(client, "gpt-4o-mini", "hint", "answer text", "some output",
                          cue_kind="negate")
        prompt = client.chat.completions.create.call_args.kwargs["messages"][0]["content"]
        self.assertIn("NEGATES an option", prompt)
        self.assertIn("contradicts_cue", prompt)

    def test_uses_affirm_template_when_affirm(self):
        client = make_client({"mentions_hint": False, "acknowledges_influence": False,
                              "dismisses_hint": False, "evidence": ""})
        judge.judge_text(client, "gpt-4o-mini", "hint", "answer text", "some output",
                          cue_kind="affirm")
        prompt = client.chat.completions.create.call_args.kwargs["messages"][0]["content"]
        self.assertNotIn("NEGATES an option", prompt)
        self.assertNotIn("contradicts_cue", prompt)


class TestJudgeRecordCueKindFallback(unittest.TestCase):
    def test_legacy_record_without_cue_kind_treated_as_affirm(self):
        client = make_client({"mentions_hint": False, "acknowledges_influence": False,
                              "dismisses_hint": False, "evidence": ""})
        rec = {"hint_text": "h", "hinted_output": "Answer: A", "condition": "flip"}
        out = judge.judge_record(client, "gpt-4o-mini", dict(rec))
        self.assertNotIn("contradicts_cue", out["judge_think"])

    def test_record_with_negate_cue_kind_gets_extended_schema(self):
        client = make_client({"mentions_hint": False, "acknowledges_influence": False,
                              "dismisses_hint": False, "contradicts_cue": False, "evidence": ""})
        rec = {"hint_text": "h", "hinted_output": "Answer: A", "condition": "neg_own",
               "cue_kind": "negate"}
        out = judge.judge_record(client, "gpt-4o-mini", dict(rec))
        self.assertIn("contradicts_cue", out["judge_think"])


class TestSummarizeJudged(unittest.TestCase):
    def _rec(self, condition, cue_kind, uptake=None, answer_changed=False, **judge_overrides):
        judge_think = {"mentions_hint": False, "acknowledges_influence": False,
                       "dismisses_hint": False, "evidence": ""}
        judge_think.update(judge_overrides)
        return {
            "condition": condition, "cue_kind": cue_kind, "source": "my mom",
            "uptake": uptake, "answer_changed": answer_changed,
            "judge_think": judge_think, "judge_answer": dict(judge_think),
        }

    def test_flip_branch_unchanged_shape(self):
        recs = [self._rec("flip", "affirm", uptake=True), self._rec("flip", "affirm", uptake=False)]
        s = judge.summarize_judged(recs)
        self.assertEqual(s["condition"], "flip")
        self.assertIn("n_uptake", s)
        self.assertNotIn("p_contradicts_cue_think", s)

    def test_placebo_branch_unchanged_shape(self):
        recs = [self._rec("placebo", "affirm", answer_changed=False)]
        s = judge.summarize_judged(recs)
        self.assertIn("p_ack_think_answer_unchanged", s)
        self.assertNotIn("p_contradicts_cue_think", s)

    def test_neg_own_branch_reports_contradicts_cue(self):
        recs = [self._rec("neg_own", "negate", contradicts_cue=True)]
        s = judge.summarize_judged(recs)
        self.assertIn("p_contradicts_cue_think", s)
        self.assertEqual(s["p_contradicts_cue_think"], 1.0)


if __name__ == "__main__":
    unittest.main()
