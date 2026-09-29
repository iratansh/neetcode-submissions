class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # return number of combinations that add to target
        # dp[i] represents the number of combinations that sum to i
        dp = [0] * (target + 1)
        dp[0] = 1

        # this problem is unbounded: can choose any amount of each num
        for i in range(1, target + 1):
            for num in nums:
                if i - num >= 0:
                    dp[i] += dp[i - num]


        return dp[target]