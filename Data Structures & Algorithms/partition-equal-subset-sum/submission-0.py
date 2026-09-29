class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # sum(sub1) == sum(sub2)
        total_sum = sum(nums)
        if total_sum % 2 != 0: return False
        targ = total_sum // 2

        dp = [False] * (targ + 1) # dp[i] represents if you can make a subset that sums to i
        dp[0] = True # empty subset sums to 0

        # iterate over all target sums -> iterate over all nums?
        # bounded problem: iterate over nums in outer loop and targs in inner loop
        for num in nums:
            for j in range(targ, num - 1, -1):
                dp[j] = (dp[j] or dp[j - num])

        return dp[targ]