class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # dp[i][j] represents the difference in scores between the 2 players for the subarray index i..j
        n = len(piles)
        dp = [[float("-inf")] * n for _ in range(n)]
        dp[n - 1][n - 1] = 0 # starting point where each player is starting at 0

        for i in range(n):
            dp[i][i] = piles[i]

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                # player can choose either piles[i] or piles[j]
                # optimally the player chooses the pile with the most rocks
                if piles[i] > piles[j]:
                    dp[i][j] = dp[i - 1][j] + piles[i]
                else:
                    dp[i][j] = dp[i][j - 1] + piles[j]


        return True if dp[0][0] > 0 else False