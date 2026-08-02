"""parsing.py is the torch-free home of classify_parse/extract_answer/
split_channels (hint_eval.py re-exports them for backward compatibility;
see tests/test_hint_eval.py for the full classify_parse behavior matrix).
This file just guards the module boundary itself: importable standalone,
with no torch/transformers dependency, and hint_eval's re-export is the
identical function object (not a divergent copy)."""

import subprocess
import sys
import unittest

import parsing


class TestModuleIsTorchFree(unittest.TestCase):
    def test_no_torch_or_transformers_imported(self):
        # Must run in a fresh subprocess: in the shared test-discovery
        # process, other test modules importing hint_eval (torch and all)
        # would already have polluted sys.modules regardless of whether
        # parsing.py itself is torch-free.
        result = subprocess.run(
            [sys.executable, "-c",
             "import parsing, sys; "
             "assert 'torch' not in sys.modules; "
             "assert 'transformers' not in sys.modules"],
            capture_output=True, text=True, cwd=__file__.rsplit("/tests/", 1)[0],
        )
        self.assertEqual(result.returncode, 0, result.stderr)


class TestHintEvalReexportsSameObjects(unittest.TestCase):
    def test_reexports_are_identical_objects(self):
        import hint_eval as he
        self.assertIs(he.classify_parse, parsing.classify_parse)
        self.assertIs(he.extract_answer, parsing.extract_answer)
        self.assertIs(he.split_channels, parsing.split_channels)


class TestBasicSmoke(unittest.TestCase):
    def test_classify_parse_explicit(self):
        self.assertEqual(parsing.classify_parse("Answer: B", 4, False), ("B", "explicit", None))

    def test_split_channels_basic(self):
        think, answer = parsing.split_channels("<think>x</think>Answer: B")
        self.assertEqual(think, "x")
        self.assertEqual(answer, "Answer: B")


if __name__ == "__main__":
    unittest.main()
