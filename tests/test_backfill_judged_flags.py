"""Tests for analysis/backfill_judged_flags.py: reclassifies existing
*.judged.jsonl files (no GPU/network — reuses backfill_parse_flags.
flag_record) and recomputes judge summaries with contains_dirty and
clean-only metrics."""

import json
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT / "analysis") not in sys.path:
    sys.path.insert(0, str(REPO_ROOT / "analysis"))

import backfill_judged_flags as bjf


def write_jsonl(path, records):
    with path.open("w") as f:
        for r in records:
            f.write(json.dumps(r) + "\n")


class TestBackfillJudgedFlags(unittest.TestCase):
    def setUp(self):
        self.tmpdir = tempfile.TemporaryDirectory()
        self.results_dir = Path(self.tmpdir.name) / "results"
        self.out_dir = Path(self.tmpdir.name) / "results_flagged"
        self.results_dir.mkdir()

        self._orig_results_dir = bjf.RESULTS_DIR
        self._orig_out_dir = bjf.OUT_DIR
        bjf.RESULTS_DIR = self.results_dir
        bjf.OUT_DIR = self.out_dir

        # 2 clean-ish (non-thinking model) + 3 truncated (thinking model,
        # no </think>) records in one judged file -> p_clean should be 2/5.
        self.judged_fp = self.results_dir / "olmo3-7b-think__my_mom__mmlu__all__flip.judged.jsonl"
        clean = [{
            "idx": i, "condition": "flip", "source": "my mom", "n_options": 4,
            "baseline_output": "<think>ok</think>Answer: A", "baseline_answer": "A",
            "hinted_output": "<think>ok</think>Answer: B", "hinted_answer": "B",
            "uptake": True, "answer_changed": True,
            "judge_think": {"mentions_hint": False, "acknowledges_influence": False},
            "judge_answer": {"mentions_hint": True, "acknowledges_influence": True},
        } for i in range(2)]
        dirty = [{
            "idx": 2 + i, "condition": "flip", "source": "my mom", "n_options": 4,
            "baseline_output": "<think>still going, (A) or (D)...",  # no </think>
            "baseline_answer": "D",
            "hinted_output": "<think>still going, (C) seems right...",  # no </think>
            "hinted_answer": "C",
            "uptake": True, "answer_changed": True,
            "judge_think": {"mentions_hint": True, "acknowledges_influence": True},
            "judge_answer": {"mentions_hint": True, "acknowledges_influence": True},
        } for i in range(3)]
        write_jsonl(self.judged_fp, clean + dirty)

    def tearDown(self):
        bjf.RESULTS_DIR = self._orig_results_dir
        bjf.OUT_DIR = self._orig_out_dir
        self.tmpdir.cleanup()

    def _load_flagged(self):
        with (self.out_dir / self.judged_fp.name).open() as f:
            return [json.loads(l) for l in f]

    def _load_summary(self):
        summary_path = self.out_dir / (self.judged_fp.stem + ".summary.json")
        with summary_path.open() as f:
            return json.load(f)

    def test_records_flagged_and_source_untouched(self):
        before = self.judged_fp.read_bytes()
        bjf.main()
        self.assertEqual(self.judged_fp.read_bytes(), before)  # results/ never modified
        flagged = self._load_flagged()
        self.assertEqual(sum(r["clean"] for r in flagged), 2)
        self.assertEqual(sum(not r["clean"] for r in flagged), 3)
        for r in flagged[2:]:  # the truncated ones
            self.assertTrue(r["think_unclosed"])
            self.assertIsNone(r["answer_strict"])

    def test_summary_has_contains_dirty_and_clean_split_metrics(self):
        bjf.main()
        summary = self._load_summary()
        self.assertTrue(summary["contains_dirty"])
        self.assertEqual(summary["n_clean"], 2)
        self.assertEqual(summary["p_clean"], 0.4)
        # clean-only recomputation: only the 2 clean records feed this.
        self.assertEqual(summary["n_uptake_clean"], 2)
        self.assertEqual(summary["p_ack_answer_given_uptake_clean"], 1.0)
        # original (all-records) metrics are still present, unrenamed.
        self.assertIn("p_ack_answer_given_uptake", summary)
        self.assertEqual(summary["n_uptake"], 5)

    def test_summary_json_filename_matches_judge_convention(self):
        bjf.main()
        self.assertTrue((self.out_dir / (self.judged_fp.stem + ".summary.json")).exists())
        # i.e. olmo3-7b-think__my_mom__mmlu__all__flip.judged.summary.json
        self.assertTrue(str(self.judged_fp.stem).endswith(".judged"))

    def test_idempotent_rerun(self):
        bjf.main()
        first = self._load_flagged()
        bjf.main()
        second = self._load_flagged()
        self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
