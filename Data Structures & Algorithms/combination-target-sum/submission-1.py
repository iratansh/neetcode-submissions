class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []

        def backtrack(i, curr, curr_sum):
            if curr_sum == target:
                res.append(curr.copy())
                return
            
            for j in range(i, len(nums)):
                if curr_sum + nums[j] > target:
                    return
                curr.append(nums[j])
                backtrack(j, curr, curr_sum + nums[j])
                curr.pop()

        backtrack(0, [], 0)
        return res