class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        # nums[i] represents the score of the ith student
        # sliding window problem? of size k?
        # window of score k, choose any scores so then sort?
        nums.sort()
        res = nums[k - 1] - nums[0]
        l = 0

        for r in range(k, len(nums)):
            l += 1
            res = min(res, nums[r] - nums[l])
            

        return res

