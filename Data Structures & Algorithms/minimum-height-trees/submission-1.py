class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return list(range(n))
        
        adj = defaultdict(list)
        indegree = [0] * n
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            indegree[u] += 1
            indegree[v] += 1

        q = deque([i for i in range(n) if indegree[i] == 1])
        
        # repeat until 2 nodes remain
        while n > 2:
            q_len = len(q)
            n -= q_len
            
            for _ in range(q_len):
                node = q.popleft()

                for nei in adj[node]:
                    indegree[nei] -= 1

                    if indegree[nei] == 1:
                        q.append(nei)
        res = []
        while q:
            res.append(q.popleft())
        return res
        
