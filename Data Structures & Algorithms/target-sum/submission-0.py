class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # returns total number of diff ways that you can build expression such that totla sum == target
        # at each position keep track of all possible sums we can form
        # how many ways each sum can be formed
        # dp[i] represents the number of ways each sum can be formed using the first i nums
        # dp[i][sum] = count
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n + 1)]
        dp[0][0] = 1

        for i in range(n):
            for total, count in dp[i].items():
                dp[i + 1][total + nums[i]] += count
                dp[i + 1][total - nums[i]] += count
        return dp[n][target]
        