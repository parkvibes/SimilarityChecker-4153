class SimilarityChecker:
    LENGTH_MAX_SCORE = 60
    def test(self, obj1, obj2):
        pass

    def length_similarity(self, obj1, obj2):

        longer = obj1 if len(obj1) > len(obj2) else obj2
        shorter = obj2 if len(obj1) > len(obj2) else obj1

        return SimilarityChecker.LENGTH_MAX_SCORE * (1 - (len(longer) - len(shorter)) / len(longer))
