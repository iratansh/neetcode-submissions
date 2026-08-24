class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # perms with dups? if there are dups then shouldn't the dup numbers resolve to the same permutations?
        # ie [1, 1, 2] should produce the same perm combinations twice for 1 since there are 2 one's? so can't we just 
        # process one 1 and then skip the other?
        res = []
        nums.sort()
        used = [False] * len(nums)

        def backtrack(path):
            if len(path) == len(nums):
                res.append(path.copy())
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue

                used[i] = True
                path.append(nums[i])

                backtrack(path)

                path.pop()
                used[i] = False
        backtrack([])
        return res