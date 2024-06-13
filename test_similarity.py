from unittest import TestCase
from similarity import SimilarityChecker


class TestSimilarityChecker(TestCase):
    def test_length_similarity(self):
        sut = SimilarityChecker()

        self.assertEqual(sut.length_similarity("abc", "abc"), 60)
        self.assertEqual(sut.length_similarity("abce", "bc"), 30)






