class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        wordDict = set(wordDict)

        def backtrack(i, path): 
            if i == len(s):
                res.append(" ".join(path))
                return
            
            # we need to segment words out from s and check if they exist in worddict?
            for j in range(i, len(s)):
                w = s[i:j + 1]
                if w in wordDict:
                    path.append(w)
                    backtrack(j + 1, path)
                    path.pop()

        backtrack(0, [])
        return res