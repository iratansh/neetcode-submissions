class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        N, M = len(matrix), len(matrix[0])
        memo = {} # (r, c): longest path from those coords

        def dfs(r, c, prevVal):
            if (not (0 <= r < N)) or (not (0 <= c < M)):
                return 0 
            if matrix[r][c] <= prevVal:
                return 0
            if (r, c) in memo:
                return memo[(r, c)]            


            res = 1
            res = max(res, 1 + dfs(r + 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r - 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r, c + 1, matrix[r][c]))
            res = max(res, 1 + dfs(r, c - 1, matrix[r][c]))
            memo[(r, c)] = res
            return res
        
        for r in range(N):
            for c in range(M):
                dfs(r, c, -1)
        return max(memo.values())