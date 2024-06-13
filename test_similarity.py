from unittest import TestCase
from similarity import SimilarityChecker


class TestSimilarityChecker(TestCase):
    def test_alphabet_similarity(self):
        a = SimilarityChecker()
        self.assertEqual(a.alphabet_similarity("ABC", "ABC"), 40)
        self.assertEqual(a.alphabet_similarity("EFG", "ABC"), 0)
