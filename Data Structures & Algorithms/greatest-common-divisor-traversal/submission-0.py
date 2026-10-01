class UnionFind:
    def __init__(self, n):
        self.n = n
        self.rank = [1] * n
        self.par = list(range(n))
    
    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]
    
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2: return False

        self.n -= 1
        if self.rank[p1] < self.rank[p2]:
            p1, p2 = p2, p1
        self.rank[p1] += self.rank[p2]
        self.par[p2] = p1
        return True
    
    def isConnected(self):
        return self.n == 1

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        # goal is to verify that all n indicies end up in a single connected component
        n = len(nums)
        uf = UnionFind(n)

        factor_idx = {} # factor: first index of factor f
        for i, n in enumerate(nums):
            f = 2
            while f * f <= n:
                if n % f == 0:
                    if f in factor_idx:
                        uf.union(i, factor_idx[f])
                    else:
                        factor_idx[f] = i
                    while n % f == 0:
                        n = n // f
                f += 1
            if n > 1:
                if n in factor_idx:
                    uf.union(i, factor_idx[n])
                else:
                    factor_idx[n] = i
        return uf.isConnected()

