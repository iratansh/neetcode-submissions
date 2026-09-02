class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        res = 0 
        count = 0
        
        def bfs():
            q = deque()
            rows, cols = len(grid), len(grid[0])

            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            nonlocal res
            nonlocal count
            
            for r in range(rows):
                for c in range(cols):
                    if grid[r][c] == 2:
                        q.append((r, c)) # start from rotten fruit and expand outwards
                    if grid[r][c] == 1:
                        count += 1
            
            while q and count > 0:
                res += 1
                for _ in range(len(q)):
                    r, c = q.popleft()
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if (nr in range(rows) and nc in range(cols) and grid[nr][nc] == 1):
                            count -= 1
                            grid[nr][nc] = 2
                            q.append((nr, nc))

        bfs()
        if not count:
            return res
        return -1


        

