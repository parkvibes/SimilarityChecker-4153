class SimilarityChecker:
    ALPHABET_MAX = 40
    def test(self, obj1, obj2):
        pass

    def alphabet_similarity(self, obj1, obj2):
        obj1_alphabet_exist = self.check_alphabet_existence(obj1)
        obj2_alphabet_exist = self.check_alphabet_existence(obj2)

        TotalCnt = self.get_total_cnt_value(obj1_alphabet_exist, obj2_alphabet_exist)
        SameCnt = self.get_same_cnt_value(obj1_alphabet_exist, obj2_alphabet_exist)

        return SameCnt / TotalCnt * SimilarityChecker.ALPHABET_MAX

    def get_same_cnt_value(self, obj1_alphabet_exist, obj2_alphabet_exist):
        return sum([1 if obj1_alphabet_exist[i] and obj2_alphabet_exist[i] else 0 for i in range(26)])

    def get_total_cnt_value(self, obj1_alphabet_exist, obj2_alphabet_exist):
        return sum([1 if obj1_alphabet_exist[i] or obj2_alphabet_exist[i] else 0 for i in range(26)])

    def check_alphabet_existence(self, obj):
        ret = []

        for i in range(26):
            ret.append(False)

        for i in range(len(obj)):
            ret[ord(obj[i]) - ord('A')] = True

        return ret





