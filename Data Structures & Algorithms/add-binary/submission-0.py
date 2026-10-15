class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # if a[i] and b[i] are both 0: stays 0
        # if a[i] and b[i] are both 1: must also keep track of carry, and the curr value is 0
        res = []
        carry = 0
        i, j = len(a) - 1, len(b) - 1

        while i >= 0 or j >= 0 or carry:
            total = carry

            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1
            dig = total % 2
            carry = total // 2

            res.append(str(dig))
        return "".join(reversed(res))        


