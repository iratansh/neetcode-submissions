class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # just find the largest island area
        self.res = 0
        ROWS, COLS = len(grid), len(grid[0])

        def bfs(r, c):
            q = deque([(r, c)])
            grid[r][c] = 0
            area = 1

            while q:
                r, c = q.popleft()
                
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = dr + r, dc + c
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                        grid[nr][nc] = 0
                        area += 1
                        q.append((nr, nc))
            self.res = max(self.res, area)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    bfs(r, c)

        return self.res