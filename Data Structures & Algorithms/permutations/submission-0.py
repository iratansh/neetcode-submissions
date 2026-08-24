class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = set()

        def backtrack(curr):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            
            for num in nums:
                if num not in visited:
                    curr.append(num)
                    visited.add(num)
                    backtrack(curr)
                    visited.remove(num)
                    curr.pop()
        backtrack([])
        return res
