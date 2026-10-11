class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        # 2 different paths to achieve the same result
        l, r = 0, 1
        res, prev = 1, "" # prev sign

        # compare pairs with the prev sign
        # 2,4,3,2,2,5,1,4
        # 2 > 4 > 3 > 2 = 2 < 5 > 1 < 4

        while r < len(arr):
            if arr[r - 1] > arr[r] and prev != ">":
                res = max(res, r - l + 1)
                r += 1
                prev = ">"
            elif arr[r - 1] < arr[r] and prev != "<":
                res = max(res, r - l + 1)
                r += 1
                prev = "<"
            else:
                r = r + 1 if arr[r] == arr[r - 1] else r
                l = r - 1
                prev = ""
        return res

        
