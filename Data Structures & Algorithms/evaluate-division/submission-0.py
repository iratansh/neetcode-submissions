class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # values[i] = equations[i][0] / equations[i][1]
        # queries[j] = [cj, dj] -> cj / dj
        # return the answer for all queries
        # a / b = value

        adj = defaultdict(list)
        for i, eq in enumerate(equations):
            a, b = eq
            adj[a].append((b, values[i]))
            adj[b].append((a, 1 / values[i]))
        
        def bfs(src, targ):
            if src not in adj or targ not in adj: return -1.0
            if src == targ: return 1.0

            visited = set()
            visited.add(src)
            q = deque([(src, 1.0)])

            while q:
                n, curr = q.popleft()
                for nei in adj[n]:
                    if nei[0] in visited:
                        continue
                    new_p = curr * nei[1]
                    if nei[0] == targ: return new_p
                    visited.add(nei[0])
                    q.append((nei[0], new_p))
            return -1.0

        res = []
        for q in queries:
            res.append(bfs(q[0], q[1]))
        return res


        