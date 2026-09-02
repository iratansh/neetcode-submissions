class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        INF = 2147483647
        
        # push all chests to the grid and then process each chest simultaneously
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
        
        while q:
            q_len = len(q)

            for _ in range(q_len):
                r, c = q.popleft()
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = dr + r, dc + c

                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == INF:
                        grid[nr][nc] = grid[r][c] + 1
                        q.append((nr, nc))
        

        
        


