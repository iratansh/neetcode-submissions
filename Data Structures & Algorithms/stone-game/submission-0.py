class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # # dp[i][j] represents the difference in scores between the 2 players for the rest of the game
        # n = len(piles)
        # dp = [[float("-inf")] * n for _ in range(n)]
        # dp[n - 1][n - 1] = 0 # starting point where each player is starting at 0

        # for i in range(n):
        #     dp[i][i] = piles[i]

        # return True if dp[0][0] > 0 else False
        return True