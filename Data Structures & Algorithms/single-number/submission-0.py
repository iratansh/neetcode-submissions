class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # dont use a set O(n) space
        
        res = 0
        for num in nums:
            res ^= num
        return res