class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for targ in range(amount + 1):
            for x in coins:
                if targ - x >= 0:
                    dp[targ] = min(dp[targ], dp[targ - x] + 1)
        return dp[amount] if dp[amount] < float("inf") else -1
