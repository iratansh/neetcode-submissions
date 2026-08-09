class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0
        left_max = 0
        right_max = 0

        while l < r:
            # height[l] is the max height in this case for calculating area
            if height[l] < height[r]:
                # update left max
                # can't update res since we are at a wall
                if left_max < height[l]:
                    left_max = height[l]
                else:
                    # calculate the water at the position
                    res += left_max - height[l]
                l += 1
            # height[r] is the max height in this case for calculating area
            else:
                # update right max
                # can't update res since we are at a wall
                if right_max < height[r]:
                    right_max = height[r]
                else:
                    res += right_max - height[r]
                r -= 1


        return res