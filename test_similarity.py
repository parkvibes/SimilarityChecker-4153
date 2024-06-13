from unittest import TestCase
from similarity import SimilarityChecker


class TestSimilarityChecker(TestCase):
    def test_length_similarity(self):
        sut = SimilarityChecker()

        self.assertEqual(sut.length_similarity("abc", "abc"), 60)
        self.assertEqual(sut.length_similarity("abce", "ebc"), 45)
        self.assertEqual(sut.length_similarity("ab", "abcddbnrd"), 0)
        self.assertEqual(sut.length_similarity("abcdddbnrd", "ab"), 0)

    def test_alphabet_similarity(self):
        a = SimilarityChecker()
        self.assertEqual(a.alphabet_similarity("ABC", "ABC"), 40)
        self.assertEqual(a.alphabet_similarity("EFG", "ABC"), 0)
