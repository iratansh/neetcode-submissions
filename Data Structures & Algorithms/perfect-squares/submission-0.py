class Solution:
    def numSquares(self, n: int) -> int:
        # dp[i] represents the least number of perfect square nums that sum to i
        dp = [float("inf")] * (n + 1)
        dp[0] = 0
        
        for targ in range(1, n + 1):
            for s in range(1, targ + 1):
                square = s * s
                if square > targ or targ - square < 0:
                    break
                
                dp[targ] = min(dp[targ], dp[targ - square] + 1)
                
        return dp[n]