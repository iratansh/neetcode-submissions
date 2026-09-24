class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # can move from current cell to adjacent cell if time >= adj cell's elevation
        N = len(grid)
        heap = [[grid[0][0], 0, 0]] # (w, r, c)
        visit = set()
        visit.add((0, 0))

        while heap:
            w, r, c = heapq.heappop(heap)

            if (r, c) == (N - 1, N - 1):
                return w

            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                nr, nc = dr + r, dc + c
                if 0 <= nr < N and 0 <= nc < N and (nr, nc) not in visit:
                    visit.add((nr, nc))
                    new_t = max(w, grid[nr][nc])
                    heapq.heappush(heap, (new_t, nr, nc))





