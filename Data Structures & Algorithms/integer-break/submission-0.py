class Solution:
    def integerBreak(self, n: int) -> int:
        # given integer n break into sum of k pos integers where k >= 2 and max the products of those ints
        # dp[i] represents the max proudct of i
        dp = [1] * (n + 1)

        for i in range(1, n + 1):
            for j in range(1, i):
                diff = i - j
                # two choices: dont break it further
                # break further
                dp[i] = max(j * diff, dp[diff] * j, dp[i])
                

        return dp[n]