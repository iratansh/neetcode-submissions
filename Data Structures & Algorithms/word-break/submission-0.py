class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp[i] represents if s[i:] can be segementsed into dict words
        word_set = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[n] = True

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n + 1):
                if s[i:j] in word_set and dp[j]:
                    dp[i] = True

        return dp[0]