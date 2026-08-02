"""Tests for analysis/uptake_analysis.py's parse-integrity handling:
clean-vs-all divergence (the "manufactured uptake" quantification),
quarantine of low-p_clean (model, dataset) cells, and the --results-dir
default/fallback behavior. Runs main() end-to-end against synthetic
fixtures in a temp directory (module globals monkeypatched, restored in
tearDown) — this mirrors how the rest of the script was hand-verified
against real data throughout development."""

import json
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT / "analysis") not in sys.path:
    sys.path.insert(0, str(REPO_ROOT / "analysis"))

import uptake_analysis as ua


def make_flip_record(idx, source, clean, uptake, parse_method="explicit", n_options=4, dataset="ds"):
    base = "A"
    hint_letter = "B"
    hinted = hint_letter if uptake else base
    return {
        "idx": idx, "condition": "flip", "dataset": dataset, "source": source,
        "n_options": n_options, "gold": "A", "gold_index": 0,
        "baseline_answer": base, "hint_letter": hint_letter, "hinted_answer": hinted,
        "hint_is_gold": False, "uptake": uptake, "answer_changed": (hinted != base),
        "clean": clean, "parse_method": parse_method,
        "base_parse_method": "explicit", "think_unclosed": False, "base_think_unclosed": False,
    }


def write_jsonl(path, records):
    with path.open("w") as f:
        for r in records:
            f.write(json.dumps(r) + "\n")


class TestCleanVsAllDivergence(unittest.TestCase):
    """The core ask: a fixture where dirty/fallback records are biased
    toward the hint letter must show rate_all > rate_clean in the
    contamination panel, and the primary table must use the clean rate."""

    def setUp(self):
        self.tmpdir = tempfile.TemporaryDirectory()
        self.root = Path(self.tmpdir.name)
        self.results_dir = self.root / "results_flagged"
        self.out_dir = self.root / "analysis"
        self.fallback_dir = self.root / "results"
        self.results_dir.mkdir()
        self.fallback_dir.mkdir()
        self._orig = dict(
            REPO_ROOT=ua.REPO_ROOT, RESULTS_DIR=ua.RESULTS_DIR, OUT_DIR=ua.OUT_DIR,
            DEFAULT_RESULTS_DIR=ua.DEFAULT_RESULTS_DIR, FALLBACK_RESULTS_DIR=ua.FALLBACK_RESULTS_DIR,
        )
        ua.REPO_ROOT = self.root
        ua.OUT_DIR = self.out_dir
        ua.DEFAULT_RESULTS_DIR = self.results_dir
        ua.FALLBACK_RESULTS_DIR = self.fallback_dir

        # 16 clean records (p_clean=0.8, NOT quarantined): 3/16 show real uptake.
        clean_records = [make_flip_record(i, "my mom", clean=True, uptake=(i < 3)) for i in range(16)]
        # 4 dirty records, ALL biased toward the hint letter (the manufactured-
        # uptake artifact: a truncated generation's fallback grabs the hinted
        # option almost every time).
        dirty_records = [
            make_flip_record(16 + i, "my mom", clean=False, uptake=True, parse_method="none")
            for i in range(4)
        ]
        write_jsonl(self.results_dir / "model-a__my_mom__ds__all__flip.jsonl", clean_records + dirty_records)

    def tearDown(self):
        for k, v in self._orig.items():
            setattr(ua, k, v)
        self.tmpdir.cleanup()

    def test_contamination_panel_shows_divergence(self):
        ua.main()
        import pandas as pd
        contamination = pd.read_csv(self.out_dir / "uptake_contamination.csv")
        row = contamination[(contamination["model"] == "model-a") & (contamination["condition"] == "flip")].iloc[0]
        self.assertEqual(row["n"], 20)
        self.assertEqual(row["n_clean"], 16)
        self.assertAlmostEqual(row["rate_all"], 7 / 20)
        self.assertAlmostEqual(row["rate_clean"], 3 / 16)
        self.assertGreater(row["rate_all"], row["rate_clean"])  # the manufactured excess

    def test_not_quarantined_and_appears_in_primary_table(self):
        ua.main()
        import pandas as pd
        integrity = pd.read_csv(self.out_dir / "uptake_parse_integrity.csv")
        row = integrity[integrity["model"] == "model-a"].iloc[0]
        self.assertFalse(bool(row["quarantined"]))
        self.assertAlmostEqual(row["p_clean"], 0.8)

        table = pd.read_csv(self.out_dir / "uptake_table.csv")
        cell = table[(table["model"] == "model-a") & (table["condition"] == "flip")].iloc[0]
        # primary table is clean-only: n should be 16, not 20, and p_uptake
        # (the legacy alias) should reflect the CLEAN rate, not the inflated one.
        self.assertEqual(cell["n"], 16)
        self.assertAlmostEqual(cell["p_uptake"], 3 / 16)


class TestQuarantine(unittest.TestCase):
    def setUp(self):
        self.tmpdir = tempfile.TemporaryDirectory()
        self.root = Path(self.tmpdir.name)
        self.results_dir = self.root / "results_flagged"
        self.out_dir = self.root / "analysis"
        self.fallback_dir = self.root / "results"
        self.results_dir.mkdir()
        self.fallback_dir.mkdir()
        self._orig = dict(
            REPO_ROOT=ua.REPO_ROOT, RESULTS_DIR=ua.RESULTS_DIR, OUT_DIR=ua.OUT_DIR,
            DEFAULT_RESULTS_DIR=ua.DEFAULT_RESULTS_DIR, FALLBACK_RESULTS_DIR=ua.FALLBACK_RESULTS_DIR,
        )
        ua.REPO_ROOT = self.root
        ua.OUT_DIR = self.out_dir
        ua.DEFAULT_RESULTS_DIR = self.results_dir
        ua.FALLBACK_RESULTS_DIR = self.fallback_dir

        # 5 clean, 15 dirty -> p_clean = 0.25 < 0.7 -> quarantined.
        clean_records = [make_flip_record(i, "my rock", clean=True, uptake=False, dataset="ds2") for i in range(5)]
        dirty_records = [
            make_flip_record(5 + i, "my rock", clean=False, uptake=True, parse_method="none", dataset="ds2")
            for i in range(15)
        ]
        write_jsonl(self.results_dir / "model-b__my_rock__ds2__all__flip.jsonl", clean_records + dirty_records)

        # a second, healthy (model, dataset) cell so quarantining model-b/ds2
        # doesn't empty the whole scope (which would just exit(1) instead of
        # exercising the "excluded but everything else proceeds" behavior).
        healthy_records = [
            make_flip_record(i, "my mom", clean=True, uptake=(i < 3), dataset="ds1") for i in range(20)
        ]
        write_jsonl(self.results_dir / "model-a__my_mom__ds1__all__flip.jsonl", healthy_records)

    def tearDown(self):
        for k, v in self._orig.items():
            setattr(ua, k, v)
        self.tmpdir.cleanup()

    def test_quarantined_cell_marked_and_excluded_from_primary_table(self):
        import pandas as pd
        ua.main()
        integrity = pd.read_csv(self.out_dir / "uptake_parse_integrity.csv")
        row = integrity[integrity["model"] == "model-b"].iloc[0]
        self.assertTrue(bool(row["quarantined"]))
        self.assertAlmostEqual(row["p_clean"], 0.25)

        table = pd.read_csv(self.out_dir / "uptake_table.csv")
        self.assertTrue(table[table["model"] == "model-b"].empty)

        report = (self.out_dir / "uptake_report.md").read_text()
        self.assertIn("model-b/ds2", report)
        self.assertIn("Quarantined", report)

    def test_quarantined_cell_still_present_in_contamination_panel(self):
        # the contamination panel is computed BEFORE quarantine filtering —
        # this is exactly where the biggest manufactured-uptake gaps live.
        import pandas as pd
        ua.main()
        contamination = pd.read_csv(self.out_dir / "uptake_contamination.csv")
        row = contamination[contamination["model"] == "model-b"]
        self.assertFalse(row.empty)
        self.assertAlmostEqual(row.iloc[0]["rate_all"], 15 / 20)
        self.assertAlmostEqual(row.iloc[0]["rate_clean"], 0.0)


class TestMissingParseFlagsFallback(unittest.TestCase):
    """No `clean` field anywhere in scope (a pre-backfill results/ directory)
    -> every record treated as clean, with a loud warning, and headline
    numbers match exactly what they'd have been before this feature existed."""

    def setUp(self):
        self.tmpdir = tempfile.TemporaryDirectory()
        self.root = Path(self.tmpdir.name)
        self.results_dir = self.root / "results_flagged"  # left empty on purpose
        self.out_dir = self.root / "analysis"
        self.fallback_dir = self.root / "results"
        self.fallback_dir.mkdir()
        self._orig = dict(
            REPO_ROOT=ua.REPO_ROOT, RESULTS_DIR=ua.RESULTS_DIR, OUT_DIR=ua.OUT_DIR,
            DEFAULT_RESULTS_DIR=ua.DEFAULT_RESULTS_DIR, FALLBACK_RESULTS_DIR=ua.FALLBACK_RESULTS_DIR,
        )
        ua.REPO_ROOT = self.root
        ua.OUT_DIR = self.out_dir
        ua.DEFAULT_RESULTS_DIR = self.results_dir
        ua.FALLBACK_RESULTS_DIR = self.fallback_dir

        records = [{
            "idx": i, "condition": "flip", "dataset": "ds", "source": "my mom",
            "n_options": 4, "gold": "A", "gold_index": 0,
            "baseline_answer": "A", "hint_letter": "B",
            "hinted_answer": "B" if i < 3 else "A",
            "hint_is_gold": False, "uptake": i < 3, "answer_changed": i < 3,
            # deliberately no clean/parse_method/think_unclosed fields at all
        } for i in range(10)]
        write_jsonl(self.fallback_dir / "model-c__my_mom__ds__all__flip.jsonl", records)

    def tearDown(self):
        for k, v in self._orig.items():
            setattr(ua, k, v)
        self.tmpdir.cleanup()

    def test_falls_back_to_raw_results_dir_and_treats_all_as_clean(self):
        import pandas as pd
        ua.main()  # no --results-dir given -> default (empty) -> fallback
        self.assertEqual(ua.RESULTS_DIR, self.fallback_dir)
        table = pd.read_csv(self.out_dir / "uptake_table.csv")
        cell = table[table["model"] == "model-c"].iloc[0]
        self.assertEqual(cell["n"], 10)  # nothing excluded — all treated as clean
        self.assertAlmostEqual(cell["p_uptake"], 3 / 10)

    def test_explicit_results_dir_bypasses_fallback_logic(self):
        ua.main(results_dir_arg=str(self.fallback_dir))
        self.assertEqual(ua.RESULTS_DIR, self.fallback_dir)


if __name__ == "__main__":
    unittest.main()
