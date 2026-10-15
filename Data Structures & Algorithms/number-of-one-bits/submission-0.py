class Solution:
    def hammingWeight(self, n: int) -> int:
        # shift 1 left 32 times since its a 32 bit int & with n to see if the bit in that pos is 1 or not
        count = 0

        for i in range(32):
            if (1 << i) & n:
                count += 1
        return count