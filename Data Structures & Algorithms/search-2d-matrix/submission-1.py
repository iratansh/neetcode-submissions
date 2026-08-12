class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # idea is to flatten out the matrix and then conduct BS
        N, M = len(matrix), len(matrix[0])
        l, r = 0, (N * M) - 1

        while l <= r:
            mid = (l + r) // 2

            row = mid // M
            col = mid % M
            val = matrix[row][col]

            if val == target:
                return True
            
            if val < target:
                l = mid + 1
            else:
                r = mid - 1
        return False