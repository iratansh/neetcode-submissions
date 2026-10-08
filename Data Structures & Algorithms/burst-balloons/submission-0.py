class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # Range DP

        # 1. Add virtual boundaries
        nums = [1] + nums + [1]

        # dp[i][j] represents the max number of coins you can recieve when bursting balloons from start position i and ending at j
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        dp[n - 1][n - 1] = 1

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                # choose a k such that i < k < j to have the the balloon to pop
                for k in range(i + 1, j):
                    dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + (nums[i] * nums[k] * nums[j]))

        return dp[0][n - 1]


