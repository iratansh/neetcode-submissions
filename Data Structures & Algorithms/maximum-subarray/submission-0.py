class Solution:
    def maxSubArray(self, nums: List[int]) -> int:  
        if len(nums) < 2:
            return nums[0]
        dp = [0] * len(nums) # dp[i] represents the max subarray sum that ends at i
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], nums[i] + dp[i - 1])

        return max(dp)