class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # treat each point as a node
        # treat the distance between every pair of points as an edge weight
        n = len(points)
        par = list(range(n + 1))
        rank = [1] * (n + 1)

        def find(i):
            if par[i] != i:
                par[i] = find(par[par[i]])
            return par[i]
        
        def union(u, v):
            pu = find(u)
            pv = find(v)
            if pu == pv:
                return False
            if rank[pu] < rank[pv]:
                pu, pv = pv, pu
            rank[pu] += rank[pv]
            par[pv] = pu
            return True
        
        edges = []
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                edges.append((dist, i, j))
        
        edges.sort()
        res = 0
        for dist, u, v in edges:
            if union(u, v):
                res += dist
        return res

        