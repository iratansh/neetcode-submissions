class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 3 pointers to the different positions? 
        l, r = 0, len(nums) - 1
        i = 0

        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]
        
        # we iterate the list using i
        while i <= r:
            # if the current num is a 0
            if nums[i] == 0:
                swap(i, l)
                l += 1
            elif nums[i] == 2:
                swap(i, r)
                r -= 1
                i -= 1
            i += 1
        