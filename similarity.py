class SimilarityChecker:
    def test(self, obj1, obj2):
        pass

    def length_similarity(self, obj1, obj2):
        if len(obj1) == len(obj2):
            return 60

        longer = obj1 if len(obj1) > len(obj2) else obj2
        shorter = obj2 if len(obj1) > len(obj2) else obj1

        return 60 * (1 - (len(longer) - len(shorter)) / len(longer))
