class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # fill out min product and max product arrays
        # min_p[i] represents the min_p only considering elements nums[0..i]
        n = len(nums)
        min_p, max_p = [1] * (n + 1), [1] * (n + 1)

        for i in range(1, n + 1):
            min_p[i] = min(nums[i - 1] * min_p[i - 1], max_p[i - 1] * nums[i - 1], nums[i - 1])
            max_p[i] = max(nums[i - 1] * min_p[i - 1], max_p[i - 1] * nums[i - 1], nums[i - 1])
    
        return max(max_p[1:])