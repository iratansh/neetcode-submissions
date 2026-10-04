class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2: 
            return 0
        
        # State 0: Holding, 1: Sold (just now), 2: Rest (available to buy)
        dp = [[0] * 3 for _ in range(n)]

        # Base Case: Day 0
        dp[0][0] = -prices[0]  # Bought it
        dp[0][1] = float('-inf') # Impossible to sell on day 0
        dp[0][2] = 0           # Started by doing nothing

        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][2] - prices[i]) # you buy today or you continue holding
            dp[i][1] = dp[i - 1][0] + prices[i]
            dp[i][2] = max(dp[i - 1][1], dp[i - 1][2]) # if you are resting then you were either resting yesterday, or you sold and are now forced into resting

        return max(dp[n - 1][1], dp[n - 1][2]) # selling should give the most profit