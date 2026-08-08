class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # sum(4 distinct combinations of nums) == target
        # two pointer approach? 
        nums.sort()
        res = []

        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # now we iterate for all j such that j starts at i and ends at nums - 2 to find the second num
            for j in range(i + 1, len(nums) - 2):
                # now we can do two pointers to find the remaining 2 nums
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue 
                l, r = j + 1, len(nums) - 1

                while l < r:
                    currSum = nums[l] + nums[r] + nums[i] + nums[j]

                    if currSum == target:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1

                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
                    elif currSum < target:
                        l += 1
                    else:
                        r -= 1
        return res