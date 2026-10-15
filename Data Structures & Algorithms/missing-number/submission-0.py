class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        xorr = n

        for i in range(n):
            xorr ^= i ^ nums[i]
        return xorr

        # a ^ a = 0
        # a ^ 0 = a
        # using this logic if we iterate through the array and continue xoring all the elements
        # the ones in the array should xor to 0 leaving only the element that is missin in the interval


        