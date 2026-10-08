class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        # player can basically take all the stones in a certain range which increases as the game progresses
        # dp[i][M] represents the max number of stones alice can get considering the subarry of piles[i..] with M 
        # M can be at most N
        n = len(piles)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        total_sum = 0
        dp[n][n] = 0

        for i in range(n - 1, -1, -1):
            total_sum += piles[i]
            for M in range(1, n + 1):
                # dp[i][M] = 0
                for X in range(1, 2 * M + 1):
                    if X + i > n:
                        break

                    dp[i][M] = max(dp[i][M], total_sum - dp[i + X][max(M, X)])
        return dp[0][1] # M starts at 1