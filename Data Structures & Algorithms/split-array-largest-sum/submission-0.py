class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # split nums into k subarrays
        # subarrays have to have >= 1 element
        # largest sum of any subarray is minimized
        # he min largest sum is the max element when k == n
        # and the max largest sum is the total sum when k == 1
        def canSplit(largest):
            subarray = 1
            currSum = 0

            for num in nums:
                currSum += num
                if currSum > largest:
                    subarray += 1
                    if subarray > k:
                        return False
                    currSum = num
            return True
        

        l, r = max(nums), sum(nums)
        res = r
        while l <= r:
            mid = (l + r) // 2

            if canSplit(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res