class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        N, M = len(heights), len(heights[0])
        heap = [[0, 0, 0]] # diff, r, c
        visited = set()
        
        while heap:
            diff, r, c = heapq.heappop(heap)

            if (r, c) in visited:
                continue
            
            visited.add((r, c))

            if (r, c) == (N - 1, M - 1):
                return diff
            
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = dr + r, dc + c
                if 0 <= nr < N and 0 <= nc < M and (nr, nc) not in visited:
                    newDiff = max(diff, abs(heights[r][c] - heights[nr][nc]))
                    heapq.heappush(heap, (newDiff, nr, nc))


