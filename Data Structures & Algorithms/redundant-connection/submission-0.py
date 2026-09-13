class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # union find: union all edges and then 
        n = len(edges)
        par = [i for i in range(n + 1)]
        rank = [1] * (n + 1)

        def find(i):
            if par[i] != i:
                par[i] = find(par[par[i]])
            return par[i]
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False
            
            r1, r2 = rank[p1], rank[p2]
            if r1 > r2:
                rank[p2] = r1
                par[p2] = p1
            else:
                rank[p1] += r2
                par[p1] = p2
        
            return True
        
        for u, v in edges:
            if not union(u, v):
                return [u, v]
        
            
        

