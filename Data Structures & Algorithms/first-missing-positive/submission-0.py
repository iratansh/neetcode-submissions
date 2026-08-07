class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # cant do sorting
        # cant use extra space
        # ans must be in the range [1, N + 1]
        # valid numbers are postiive - must use cyclic sort to place each int at postion x - 1
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                correct_idx = nums[i] - 1
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
        
        # Second pass: find the first position missing its expected value
        
        for i in range(n):
            x = nums[i]
            if x != i + 1:
                return i + 1
        return n + 1