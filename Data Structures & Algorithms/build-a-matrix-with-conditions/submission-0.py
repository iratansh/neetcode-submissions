class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        # build a k x k matrix that contains each of the values (1 to k) exactly once
        # remaining cells should have 0
        def topo_sort(conditions, k):
            adj = defaultdict(list)
            indegree = [0] * (k + 1)
            for u, v in conditions:
                adj[u].append(v)
                indegree[v] += 1
            
            q = deque([i for i in range(1, k + 1) if indegree[i] == 0])
            res = []
            while q:
                node = q.popleft()
                res.append(node)
                for nei in adj[node]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        q.append(nei)
            return res if len(res) == k else []
        
        rowPos = topo_sort(rowConditions, k)
        colPos = topo_sort(colConditions, k)
        if not rowPos or not colPos: return []
        matrix = [[0] * k for _ in range(k)]
        row_map = {num: r for r, num in enumerate(rowPos)}
        col_map = {num: c for c, num in enumerate(colPos)}

        for num in range(1, k + 1):
            matrix[row_map[num]][col_map[num]] = num
        return matrix