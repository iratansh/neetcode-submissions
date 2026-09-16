class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, t in times:
            adj[u].append((v, t))
        
        heap = [(0, k)]
        vis = set()
        t = 0

        while heap:
            w1, n1 = heapq.heappop(heap)
            if n1 in vis:
                continue
            vis.add(n1)
            t = w1

            for n2, w2 in adj[n1]:
                if n2 not in vis:
                    heapq.heappush(heap, (w1 + w2, n2))
        
        return t if len(vis) == n else -1

