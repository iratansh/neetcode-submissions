class DisjointSet:
    def __init__(self, n):
        self.par = list(range(n))
        self.rank = [1] * n
    
    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[self.par[x]])
        return self.par[x]
    
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2: return False

        r1, r2 = self.rank[p1], self.rank[p2]
        if r1 > r2:
            self.par[p2] = p1
        elif r1 < r2:
            self.par[p1] = p2
        else:
            self.par[p2] = p1
            self.rank[p1] += 1
        return True

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # Kruskal + DSU
        # preserve original index ordering
        for i in range(len(edges)):
            edges[i].append(i)
        edges.sort(key=lambda x:x[2])
        dsu = DisjointSet(n)

        total_weight = 0
        added = 0

        for u, v, w, i in edges:
            if dsu.union(u, v):
                total_weight += w
        
        crit, pseudo = [], []
        for n1, n2, e_weight, i in edges:
            # try without curr edge
            weight = 0
            uf = DisjointSet(n)
            for v1, v2, w, j in edges:
                if i != j and uf.union(v1, v2):
                    weight += w
            if sum(1 for k in range(n) if uf.find(k) == k) > 1 or weight > total_weight:
                crit.append(i)
                continue

            # try with current edge
            uf = DisjointSet(n)
            uf.union(n1, n2)
            weight = e_weight
            for v1, v2, w, j in edges:
                if uf.union(v1, v2):
                    weight += w
            if weight == total_weight:
                pseudo.append(i)
        return [crit, pseudo]
            