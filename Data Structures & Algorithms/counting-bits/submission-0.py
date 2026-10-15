class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)

        for i in range(n + 1):
            count = 0
            for j in range(32):
                if (1 << j) & i:
                    count += 1
            res[i] = count
        return res

