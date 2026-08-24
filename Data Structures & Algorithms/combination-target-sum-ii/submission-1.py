class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtrack(i, curr, curr_sum):
            if curr_sum == target:
                res.append(curr.copy())
                return
            
            for j in range(i, len(candidates)):
                if curr_sum + candidates[j] > target:
                    return
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                
                curr.append(candidates[j])
                backtrack(j + 1, curr, curr_sum + candidates[j])
                curr.pop()

        backtrack(0, [], 0)
        return res
        