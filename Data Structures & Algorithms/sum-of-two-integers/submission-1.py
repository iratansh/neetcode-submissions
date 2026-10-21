class Solution:
    def getSum(self, a: int, b: int) -> int:
        # to get the sum of 2 ints we would need to add their bits
        mask = 0xFFFFFFFF

        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & mask

            b = carry & mask
        return a if a <= 0x7FFFFFFF else ~(a ^ mask)