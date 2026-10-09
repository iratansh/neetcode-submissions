class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # either take the current char or skip it? 
        # run a dfs starting from i = 0 and j = 0
        memo = {} # (i, j): number of ways to form t[j:] from s[i:]
        N, M = len(s), len(t)

        if M > N: return 0

        # i corresponds to s and j corresponds to t
        def dfs(i, j):
            if j == M:
                return 1
            if i == N:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]

            res = dfs(i + 1, j)
            if s[i] == t[j]:
                res += dfs(i + 1, j + 1)

            memo[(i, j)] = res
            return res
        
        return dfs(0, 0)


