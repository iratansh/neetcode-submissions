class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 1. Build Adj List and Indegree Array
        adj = {i: [] for i in range(numCourses)}
        indegree = [0] * numCourses

        for crs, pre in prerequisites:
            adj[pre].append(crs) # pre points to crs
            indegree[crs] += 1   # crs has one more dependency
            
        def bfs():  
            q = deque()
            finished = 0
            for i in range(numCourses):
                if indegree[i] == 0:
                    q.append(i)
            
            while q:
                c = q.popleft()
                finished += 1
                for next in adj[c]:
                    indegree[next] -= 1
                    if indegree[next] == 0:
                        q.append(next)
            return finished
        
        return bfs() == numCourses