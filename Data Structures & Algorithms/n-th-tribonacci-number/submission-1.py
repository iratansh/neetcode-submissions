class Solution:
    def tribonacci(self, n: int) -> int:
        # tn+3 = tn + tn+1 + tn+2
        # dp[i] represents the results of the ith tribonnaci
        if n == 1: return 1
        if n == 0: return 0
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 1
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

        return dp[n]