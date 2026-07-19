"""Unit tests for qa_datasets normalization logic.

Uses hand-built rows mimicking each dataset's raw HF schema — no network or
GPU required. Run with: python -m pytest tests/ -q  (or python -m unittest).
"""

import unittest

from qa_datasets import (
    _normalize_agieval,
    _normalize_gsm_mc,
    _normalize_logiqa2,
    _normalize_medqa,
    _normalize_mmlu_pro,
    validate_subset,
)


class TestMmluPro(unittest.TestCase):
    def test_normalizes_ok_row(self):
        row = {
            "question": "What is 2+2?",
            "options": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
            "answer_index": 3,
        }
        item = _normalize_mmlu_pro(42, row, "math")
        self.assertEqual(item["answer"], 3)
        self.assertEqual(item["choices"][3], "4")
        self.assertEqual(item["qid"], "mmlu_pro:math:42")

    def test_drops_fewer_than_4_options(self):
        row = {"question": "Q", "options": ["a", "b", "c"], "answer_index": 0}
        self.assertIsNone(_normalize_mmlu_pro(0, row, None))

    def test_subset_none_uses_all_in_qid(self):
        row = {"question": "Q", "options": ["a", "b", "c", "d"], "answer_index": 1}
        item = _normalize_mmlu_pro(7, row, None)
        self.assertEqual(item["qid"], "mmlu_pro:all:7")


class TestMedQA(unittest.TestCase):
    def test_letter_to_index_mapping(self):
        row = {
            "question": "A patient presents with...",
            "options": {"A": "Do nothing", "B": "Correct answer", "C": "Wrong", "D": "Also wrong"},
            "answer_idx": "B",
        }
        item = _normalize_medqa(3, row, None)
        self.assertEqual(item["answer"], 1)
        self.assertEqual(item["choices"], ["Do nothing", "Correct answer", "Wrong", "Also wrong"])
        self.assertEqual(item["qid"], "medqa:all:3")

    def test_out_of_order_dict_still_sorts_by_letter(self):
        row = {"question": "Q", "options": {"C": "c", "A": "a", "B": "b"}, "answer_idx": "C"}
        item = _normalize_medqa(0, row, None)
        self.assertEqual(item["choices"], ["a", "b", "c"])
        self.assertEqual(item["answer"], 2)

    def test_missing_answer_idx_skipped(self):
        row = {"question": "Q", "options": {"A": "a", "B": "b"}, "answer_idx": None}
        self.assertIsNone(_normalize_medqa(0, row, None))

    def test_answer_letter_not_in_options_skipped(self):
        row = {"question": "Q", "options": {"A": "a", "B": "b"}, "answer_idx": "Z"}
        self.assertIsNone(_normalize_medqa(0, row, None))


class TestLogiQA2(unittest.TestCase):
    def test_passage_prepended(self):
        row = {
            "text": "Some passage about logic.",
            "question": "Which conclusion follows?",
            "options": ["opt1", "opt2", "opt3", "opt4"],
            "answer": 2,
        }
        item = _normalize_logiqa2(5, row, None)
        self.assertTrue(item["question"].startswith("Some passage about logic.\n\n"))
        self.assertTrue(item["question"].endswith("Which conclusion follows?"))
        self.assertEqual(item["answer"], 2)
        self.assertEqual(item["qid"], "logiqa2:all:5")

    def test_missing_passage_no_double_newline(self):
        row = {"text": "", "question": "Q only", "options": ["a", "b"], "answer": 0}
        item = _normalize_logiqa2(0, row, None)
        self.assertEqual(item["question"], "Q only")

    def test_out_of_range_answer_skipped(self):
        row = {"text": "", "question": "Q", "options": ["a", "b"], "answer": 5}
        self.assertIsNone(_normalize_logiqa2(0, row, None))


class TestGsmMc(unittest.TestCase):
    def test_normalizes_ab_cd_row(self):
        row = {"A": "22", "B": "64", "C": "18", "D": "12", "Answer": "C", "Question": "How many eggs?"}
        item = _normalize_gsm_mc(9, row, None)
        self.assertEqual(item["choices"], ["22", "64", "18", "12"])
        self.assertEqual(item["answer"], 2)
        self.assertEqual(item["qid"], "gsm_mc:all:9")

    def test_answer_letter_out_of_range_skipped(self):
        row = {"A": "1", "B": "2", "C": "3", "D": "4", "Answer": "E", "Question": "Q"}
        self.assertIsNone(_normalize_gsm_mc(0, row, None))

    def test_missing_question_skipped(self):
        row = {"A": "1", "B": "2", "C": "3", "D": "4", "Answer": "A", "Question": ""}
        self.assertIsNone(_normalize_gsm_mc(0, row, None))


class TestAgieval(unittest.TestCase):
    def test_strips_parenthesised_letter_prefix(self):
        row = {
            "query": "Q: what?",
            "choices": ["(A)first", "(B)second", "(C)third", "(D)fourth"],
            "gold": [1],
        }
        item = _normalize_agieval(1, row, "lsat-lr")
        self.assertEqual(item["choices"], ["first", "second", "third", "fourth"])
        self.assertEqual(item["answer"], 1)
        self.assertEqual(item["qid"], "agieval:lsat-lr:1")

    def test_strips_letter_dot_prefix(self):
        row = {"query": "Q", "choices": ["A. one", "B. two"], "gold": [0]}
        item = _normalize_agieval(0, row, "sat-math")
        self.assertEqual(item["choices"], ["one", "two"])

    def test_multi_gold_skipped(self):
        row = {"query": "Q", "choices": ["(A)a", "(B)b"], "gold": [0, 1]}
        self.assertIsNone(_normalize_agieval(0, row, "lsat-ar"))

    def test_empty_gold_skipped(self):
        row = {"query": "Q", "choices": ["(A)a", "(B)b"], "gold": []}
        self.assertIsNone(_normalize_agieval(0, row, "lsat-ar"))

    def test_no_prefix_left_unchanged(self):
        row = {"query": "Q", "choices": ["already clean", "also clean"], "gold": [0]}
        item = _normalize_agieval(0, row, "lsat-ar")
        self.assertEqual(item["choices"], ["already clean", "also clean"])


class TestValidateSubset(unittest.TestCase):
    def test_mmlu_requires_subset(self):
        with self.assertRaises(ValueError):
            validate_subset("mmlu", None)
        validate_subset("mmlu", "high_school_psychology")  # should not raise

    def test_none_datasets_reject_subset(self):
        for ds in ["medqa", "logiqa2", "gsm_mc"]:
            with self.assertRaises(ValueError):
                validate_subset(ds, "something")
            validate_subset(ds, None)  # should not raise

    def test_mmlu_pro_subset_optional(self):
        validate_subset("mmlu_pro", None)
        validate_subset("mmlu_pro", "law")

    def test_agieval_rejects_unknown_subset(self):
        with self.assertRaises(ValueError):
            validate_subset("agieval", "not-a-real-task")
        validate_subset("agieval", "lsat-ar")
        validate_subset("agieval", None)  # default applied later by load_qa

    def test_unknown_dataset_rejected(self):
        with self.assertRaises(ValueError):
            validate_subset("not-a-dataset", None)


if __name__ == "__main__":
    unittest.main()
