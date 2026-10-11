class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # end of array connects to beginning of the array 
        # case 1: max subarray does not wrap around
        # case 2: max subarray wraps around - if the ends make up a max subarray sum then what's in the middle makes up a min subarray array sum total sum - minsum = max sum
        curr_max = max_subarray = nums[0]
        curr_min = min_subarray = nums[0]
        total_sum = sum(nums) 

        for num in nums[1:]:
            curr_min = min(num, curr_min + num)
            curr_max = max(num, curr_max + num)

            min_subarray = min(min_subarray, curr_min)
            max_subarray = max(max_subarray, curr_max)

        if max_subarray < 0: return max_subarray
        return max(max_subarray, total_sum - min_subarray)
