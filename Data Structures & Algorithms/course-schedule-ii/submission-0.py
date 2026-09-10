class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i: [] for i in range(numCourses)}
        indegree = [0] * numCourses
        for crs, pre in prerequisites:
            adj[pre].append(crs)
            indegree[crs] += 1

        res = []
        def bfs():
            q = deque()
            for i in range(numCourses):
                if indegree[i] == 0:
                    q.append(i)
            
            while q:
                c = q.popleft()
                res.append(c)

                for next in adj[c]:
                    indegree[next] -= 1
                    if indegree[next] == 0:
                        q.append(next)

        bfs()
        if len(res) == numCourses:
            return res
        return []