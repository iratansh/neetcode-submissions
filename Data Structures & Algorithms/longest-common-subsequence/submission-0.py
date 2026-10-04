class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # dp[i][j] represents the length of the longest common subsequence between text1[0...i-1] and text2[0...j-1]
        n, m = len(text1), len(text2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        # base case: dp[0][j] = 0 for all j < m and dp[i][0] = 0 for all i < n
        # already set

        # want to compare the characters at text1[i] and text2[j]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[n][m]
