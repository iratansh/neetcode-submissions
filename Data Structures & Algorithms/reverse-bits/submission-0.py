class Solution:
    def reverseBits(self, n: int) -> int:
        # extrac the bit in the LST if its a 1 and update the corresponding bit in res
        res = 0

        for i in range(32):
            # get the ith bit as the LSB
            if (n >> i) & 1:
                res |= 1 << (31 - i)
        return res
