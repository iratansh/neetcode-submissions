class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        # dp[i] represents the state of the game from stoneValues[i...n - 1]
        # dp[i] represents the maximum margin of victory (current player's score - opponent's score) achievable from the subgame starting at index i
        n = len(stoneValue)
        dp = [float("-inf")] * (n + 1)
        dp[n] = 0 # represents state of the game when no stones are left

        for i in range(n - 1, -1, -1):
            tot = 0
            for j in range(i, min(i + 3, n)):
                tot += stoneValue[j]
                dp[i] = max(dp[i], tot - dp[j + 1])

        if dp[0] > 0: return "Alice"
        if dp[0] < 0: return "Bob"
        return "Tie"