class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # dp[i][j] represents the numebr of distinct subsequences of s[0...i] which are equal to t[0...j]
        dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]

        # base case: 
        # dp[i][0] has to equal 1 for all i since there's one way to form an empty string only using chars in s (choose nothing)
        # dp[0][j] has to equal 0 for all j

        for i in range(len(s) + 1):
            dp[i][0] = 1

        for i in range(1, len(s) + 1):
            for j in range(1, len(t) + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[len(s)][len(t)]
