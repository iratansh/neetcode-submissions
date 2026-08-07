class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p1, p2 = 0, 0
        n1, n2 = len(word1), len(word2)
        res = ""

        while p1 < n1 and p2 < n2:
            res += word1[p1]
            res += word2[p2]
            p1 += 1
            p2 += 1
        
        # check if there are any extra characters left
        while p1 < n1:
            res += word1[p1]
            p1 += 1
        while p2 < n2:
            res += word2[p2]
            p2 += 1
        return res
