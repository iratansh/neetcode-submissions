class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # need to check if border is water or not
        ROWS, COLS = len(grid), len(grid[0])

        def bfs(r, c):
            q = deque([(r, c)])
            vis = set()
            vis.add((r, c))
            res = 0

            while q:
                r, c = q.popleft()

                for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    nr, nc = dr + r, dc + c
                    if (nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == 0):
                        res += 1
                    elif (nr, nc) not in vis:
                        q.append((nr, nc))
                        vis.add((nr, nc))
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return bfs(r, c)
        return 0