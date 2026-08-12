class Solution:
    def findMin(self, nums: List[int]) -> int:
        # need to find sorted portion of the array and then narrow down search from there?
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            # element to the right of nums[r]
            if nums[r] < nums[mid]:
                l = mid + 1
            else:
                r = mid

        return nums[l]