class SimilarityChecker:
    def test(self, obj1, obj2):
        pass

    def alphabet_similarity(self, obj1, obj2):
        obj1_alphabet_exist = []
        obj2_alphabet_exist = []

        for i in range(26):
            obj1_alphabet_exist.append(False)
            obj2_alphabet_exist.append(False)

        for i in range(len(obj1)):
            obj1_alphabet_exist[ord(obj1[i]) - ord('A')] = True

        for i in range(len(obj2)):
            obj2_alphabet_exist[ord(obj2[i]) - ord('A')] = True

        TotalCnt = sum([1 if obj1_alphabet_exist[i] or obj2_alphabet_exist[i] else 0 for i in range(26)])
        SameCnt = sum([1 if obj1_alphabet_exist[i] and obj2_alphabet_exist[i] else 0 for i in range(26)])

        return SameCnt / TotalCnt * 40





