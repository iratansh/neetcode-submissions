class Solution:
    def jump(self, nums: List[int]) -> int:
        # this time return the minimum number of jumps to reach the last position
        if len(nums) < 2:
            return 0

        max_reach = 0
        current_jump_end = 0
        res = 0
        for i in range(len(nums)):
            max_reach = max(max_reach, nums[i] + i) # max reach is still the furthest index we can currently go 
            if i == current_jump_end: # only when we reach the end of our current jump end
                res += 1 # do we increment res
                current_jump_end = max_reach # and then update the current jump end to the max reach
                
            if current_jump_end >= len(nums) - 1: # if we can reach the end of the list within the same jump we can return res
                break  
        
        return res
        


        