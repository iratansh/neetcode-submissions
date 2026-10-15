class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # dont use a set O(n) space
        # all numbers that appear twice will cancel eachother out
        # leaving the number that apepars once
        res = 0
        for num in nums:
            res ^= num
        return res