class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp[i] represents the longest increasing subsequence only considering nums[0..i]
        n = len(nums)
        dp = [1] * n

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)