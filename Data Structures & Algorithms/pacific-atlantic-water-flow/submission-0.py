class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac = set()
        atl = set()

        def bfs(coords):
            # add all cords to the queue and then for a bfs on it
            q = deque()

            for coord in coords:
                q.append(coord)
            
            while q:
                q_len = len(q)

                for _ in range(q_len):
                    r, c = q.popleft()

                    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        nr, nc = dr + r, dc + c
                        if 0 <= nr < ROWS and 0 <= nc < COLS and heights[nr][nc] >= heights[r][c] and (nr, nc) not in coords:
                            q.append((nr, nc))
                            coords.add((nr, nc))

        # want to call bfs from the borders of pac and atl and then find the union of pac and atl sets to find the res coordinates
        for r in range(ROWS):
            pac.add((r, 0))
            atl.add((r, COLS - 1))
        
        for c in range(COLS):
            pac.add((0, c))
            atl.add((ROWS - 1, c))
        
        bfs(pac)
        bfs(atl)

        res = []
        for coord in atl:
            if coord in pac:
                res.append(coord)
        return res





