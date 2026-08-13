class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()

        # 1. Find Peak Index
        l, r = 1, n - 2
        peak = -1
        
        while l <= r:
            mid = (l + r) // 2
            left_val = mountainArr.get(mid - 1)
            mid_val = mountainArr.get(mid)        # Use distinct variable name
            right_val = mountainArr.get(mid + 1)
            
            if left_val < mid_val < right_val:
                l = mid + 1
            elif left_val > mid_val > right_val:
                r = mid - 1
            else:
                peak = mid                        # Found peak index
                break

        # 2. Search strictly increasing left side (0 to peak)
        l, r = 0, peak
        while l <= r:
            mid = (l + r) // 2
            val = mountainArr.get(mid)

            if val < target:
                l = mid + 1
            elif val > target:
                r = mid - 1
            else:
                return mid  # Always return minimum index first

        # 3. Search strictly decreasing right side (peak + 1 to n - 1)
        l, r = peak + 1, n - 1
        while l <= r:
            mid = (l + r) // 2
            val = mountainArr.get(mid)

            if val > target:        # Reverse logic for decreasing array
                l = mid + 1
            elif val < target:
                r = mid - 1
            else:
                return mid

        return -1