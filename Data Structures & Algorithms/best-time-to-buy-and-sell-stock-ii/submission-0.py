class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dp[i][0] is the max amount of profit when we buy
        # dp[i][1] is the max anount of profit when we sell
        n = len(prices)
        dp = [[0] * 2 for _ in range(n + 1)]
        dp[0][0] = float("-inf") # holding a stock before day 0 is impossible

        # dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] - prices[i - 1])
        # dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i - 1])
        for i in range(1, n + 1):
            price = prices[i - 1]
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] - prices[i - 1])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i - 1])
        return dp[n][1] # max profit is the day we sell

