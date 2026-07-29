"""Tests for analysis/backfill_parse_flags.py against 3 hand-built jsonl
fixtures (clean, truncated-think, fallback-nonthink) — no GPU/network.
Verifies flags, answer_strict, parse_changed, and that results/ is never
modified (checksum before/after)."""

import hashlib
import importlib
import json
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))
if str(REPO_ROOT / "analysis") not in sys.path:
    sys.path.insert(0, str(REPO_ROOT / "analysis"))

import backfill_parse_flags as bpf


def sha256_of(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_jsonl(path, records):
    with path.open("w") as f:
        for r in records:
            f.write(json.dumps(r) + "\n")


class TestBackfillParseFlags(unittest.TestCase):
    """3 fixtures:
      1. clean.jsonl              — non-thinking model, explicit both sides
      2. truncated_think.jsonl    — thinking model, no </think> (the bug)
      3. fallback_nonthink.jsonl  — non-thinking model, parenthesis-only
    """

    def setUp(self):
        self.tmpdir = tempfile.TemporaryDirectory()
        self.results_dir = Path(self.tmpdir.name) / "results"
        self.out_dir = Path(self.tmpdir.name) / "results_flagged"
        self.results_dir.mkdir()

        self._orig_results_dir = bpf.RESULTS_DIR
        self._orig_out_dir = bpf.OUT_DIR
        bpf.RESULTS_DIR = self.results_dir
        bpf.OUT_DIR = self.out_dir

        # --- fixture 1: clean (non-thinking model) ---
        self.clean_fp = self.results_dir / "olmo3-7b-instruct__my_mom__mmlu__all__flip.jsonl"
        write_jsonl(self.clean_fp, [{
            "idx": 0, "condition": "flip", "n_options": 4,
            "baseline_output": "reasoning...\nAnswer: A", "baseline_answer": "A",
            "hinted_output": "reasoning...\nAnswer: B", "hinted_answer": "B",
            "uptake": True,
        }])
        (self.results_dir / "olmo3-7b-instruct__my_mom__mmlu__all__flip.summary.json").write_text(
            json.dumps({"model": "olmo3-7b-instruct", "n": 1, "p_uptake": 1.0}))

        # --- fixture 2: truncated-think (thinking model, the manufactured-
        # uptake bug: old fallback-enabled parsing grabbed "C" from the
        # unfinished scratchpad; no </think> anywhere) ---
        self.truncated_fp = self.results_dir / "olmo3-7b-think__my_mom__mmlu__all__flip.jsonl"
        write_jsonl(self.truncated_fp, [{
            "idx": 0, "condition": "flip", "n_options": 4,
            "baseline_output": "<think>still reasoning, (A) or maybe (D)...",
            "baseline_answer": "D",
            "hinted_output": "<think>still going, (C) seems right but wait...",
            "hinted_answer": "C",
            "uptake": True,
        }])
        (self.results_dir / "olmo3-7b-think__my_mom__mmlu__all__flip.summary.json").write_text(
            json.dumps({"model": "olmo3-7b-think", "n": 1, "p_uptake": 1.0}))

        # --- fixture 3: fallback-nonthink (non-thinking model, parenthesis
        # only, no "Answer:" literal — fallback stays valid for these) ---
        self.fallback_fp = self.results_dir / "qwen3-8b-nothink__my_mom__mmlu__all__flip.jsonl"
        write_jsonl(self.fallback_fp, [{
            "idx": 0, "condition": "flip", "n_options": 4,
            "baseline_output": "so it must be (A) given the context",
            "baseline_answer": "A",
            "hinted_output": "so it must be (B) given the hint",
            "hinted_answer": "B",
            "uptake": True,
        }])
        (self.results_dir / "qwen3-8b-nothink__my_mom__mmlu__all__flip.summary.json").write_text(
            json.dumps({"model": "qwen3-8b-nothink", "n": 1, "p_uptake": 1.0}))

        self.checksums_before = {
            fp: sha256_of(fp) for fp in self.results_dir.glob("*")
        }

    def tearDown(self):
        bpf.RESULTS_DIR = self._orig_results_dir
        bpf.OUT_DIR = self._orig_out_dir
        self.tmpdir.cleanup()

    def _load_flagged(self, name):
        with (self.out_dir / name).open() as f:
            return json.loads(f.readline())

    def test_source_files_untouched(self):
        bpf.main()
        for fp, checksum_before in self.checksums_before.items():
            self.assertEqual(sha256_of(fp), checksum_before, f"{fp} was modified!")

    def test_clean_fixture_flagged_clean_no_change(self):
        bpf.main()
        r = self._load_flagged(self.clean_fp.name)
        self.assertEqual(r["parse_method"], "explicit")
        self.assertEqual(r["base_parse_method"], "explicit")
        self.assertTrue(r["clean"])
        self.assertEqual(r["answer_strict"], "B")
        self.assertEqual(r["baseline_answer_strict"], "A")
        self.assertFalse(r["parse_changed"])
        self.assertFalse(r["baseline_parse_changed"])
        self.assertIsNone(r["think_unclosed"])  # non-thinking model

    def test_truncated_think_fixture_nulls_manufactured_answer(self):
        bpf.main()
        r = self._load_flagged(self.truncated_fp.name)
        self.assertEqual(r["parse_method"], "none")
        self.assertEqual(r["base_parse_method"], "none")
        self.assertTrue(r["think_unclosed"])
        self.assertTrue(r["base_think_unclosed"])
        self.assertFalse(r["clean"])
        self.assertIsNone(r["answer_strict"])
        self.assertIsNone(r["baseline_answer_strict"])
        # the key assertion: old hinted_answer="C" was manufactured by the
        # fallback reading scratchpad text; answer_strict correctly nulls it,
        # and parse_changed flags the discrepancy, WITHOUT touching hinted_answer.
        self.assertEqual(r["hinted_answer"], "C")  # provenance preserved
        self.assertEqual(r["baseline_answer"], "D")  # provenance preserved
        self.assertTrue(r["parse_changed"])
        self.assertTrue(r["baseline_parse_changed"])

    def test_fallback_nonthink_fixture_stays_valid_but_not_clean(self):
        bpf.main()
        r = self._load_flagged(self.fallback_fp.name)
        self.assertEqual(r["parse_method"], "fallback")
        self.assertEqual(r["base_parse_method"], "fallback")
        self.assertFalse(r["clean"])  # fallback != explicit, so not clean
        self.assertEqual(r["answer_strict"], "B")  # fallback answer preserved for non-thinking
        self.assertEqual(r["baseline_answer_strict"], "A")
        self.assertFalse(r["parse_changed"])  # matches what was already stored
        self.assertFalse(r["baseline_parse_changed"])
        self.assertIsNone(r["think_unclosed"])

    def test_summary_json_merges_original_and_new_fields(self):
        bpf.main()
        with (self.out_dir / "olmo3-7b-instruct__my_mom__mmlu__all__flip.summary.json").open() as f:
            summ = json.load(f)
        self.assertEqual(summ["model"], "olmo3-7b-instruct")  # original field preserved
        self.assertEqual(summ["n_clean"], 1)
        self.assertEqual(summ["p_clean"], 1.0)
        self.assertTrue(summ["has_parse_flags"])

    def test_uptake_rate_all_vs_clean_diverges_on_truncated_file(self):
        bpf.main()
        with (self.out_dir / (self.truncated_fp.stem + ".summary.json")).open() as f:
            summ = json.load(f)
        # uptake_all reflects the (manufactured) stored uptake=True;
        # uptake_clean has zero clean records to average over -> nan.
        self.assertEqual(summ["uptake_rate_all"], 1.0)
        self.assertTrue(summ["uptake_rate_clean"] != summ["uptake_rate_clean"])  # NaN

    def test_idempotent_rerun_produces_identical_output(self):
        bpf.main()
        first = self._load_flagged(self.clean_fp.name)
        bpf.main()
        second = self._load_flagged(self.clean_fp.name)
        self.assertEqual(first, second)

    def test_judged_files_skipped(self):
        judged_fp = self.results_dir / "olmo3-7b-instruct__my_mom__mmlu__all__flip.judged.jsonl"
        write_jsonl(judged_fp, [{"idx": 0}])
        bpf.main()
        self.assertFalse((self.out_dir / judged_fp.name).exists())


if __name__ == "__main__":
    unittest.main()
