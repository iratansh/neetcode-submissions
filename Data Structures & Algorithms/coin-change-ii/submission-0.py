class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # unlimited amount of coins? dp[i] represents the number of ways to form amount i
        dp = [0] * (amount + 1) 
        dp[0] = 1

        # iterate from all coins backwards to build the res
        for i in range(len(coins) - 1, -1, -1):
            for amt in range(1, amount + 1):
                if coins[i] <= amt:
                    dp[amt] += dp[amt - coins[i]]

        return dp[amount]

