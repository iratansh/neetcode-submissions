class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # goal is to mimize the last possible weight of last stone
        # meaning we want to seperate stones into 2 groups such that the difference of the sum of stones in each group is minimized?
        # minimizing final weight = finding sum of stones whos value is closest to sum(stones) // 2
        # dp[i][j] represents the total maximum weight <= j you can form using a subset of stones[0..i]

        # 0/1 knapsack: take it or leave it dp
        # loop through all stones, and all capacities up to targ
        n = len(stones)
        stoneSum = sum(stones)
        targ = stoneSum // 2
        dp = [[0] * (targ + 1) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            for j in range(1, targ + 1):
                w = stones[i - 1]
                if j >= w:
                    # leave it = dp[i-1][j], take it = dp[i-1][j-w] + w
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + w)
                else:
                    dp[i][j] = dp[i - 1][j]
        return stoneSum - 2 * dp[n][targ]