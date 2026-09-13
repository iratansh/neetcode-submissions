class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)

        for pre, crs in prerequisites:
            adj[crs].append(pre)    
        
        # idea is to run a dfs from each crs to idenitfy its prereqs?
        def dfs(crs):
            if crs in prereqMap:
                return prereqMap[crs]
                
            for prereq in adj[crs]:
                prereqMap[crs] |= dfs(prereq)
            prereqMap[crs].add(crs)
            return prereqMap[crs]

        prereqMap = defaultdict(set)
        for i in range(numCourses):
            dfs(i)

        res = []
        for u, v in queries:
            if u in prereqMap[v]:
                res.append(True)
            else:
                res.append(False)
        return res
        
