class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []

        def backtrack(i, curr, curr_sum):
            if curr_sum == target:
                res.append(curr.copy())
                return
            if i >= len(nums) or curr_sum > target:   
                return
            
            curr.append(nums[i])
            backtrack(i, curr, curr_sum + nums[i]) # take nums[i]
            curr.pop()
            backtrack(i + 1, curr, curr_sum) # leave nums[i]

        backtrack(0, [], 0)
        return res