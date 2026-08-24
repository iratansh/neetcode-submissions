class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        # backtracking subsets problem
        self.res = 0

        def backtrack(i, curr):
            xorr = 0
            for num in curr:
                xorr ^= num
            self.res += xorr

            for j in range(i, len(nums)):
                curr.append(nums[j])
                backtrack(j + 1, curr)
                curr.pop()
            

        backtrack(0, [])
        return self.res
        


