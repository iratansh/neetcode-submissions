class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # initially w capital -> sort by capital
        n = len(profits)
        sorted_projects = [(capital[i], profits[i], i) for i in range(n)]
        sorted_projects.sort(key=lambda x:x[0])
        
        # iterate through sorted_projects: choose the projects that have a capital <= curr_cap and append to max heap?
        # max heap pulls the projects that produce the highest capital so we can maixmize capital based off k projects?
        curr_cap = w
        heap = [] # max heap
        i = 0 # pointer to sorted_projects: push all newly affordably projects to the heap

        for _ in range(k):
            while i < n and sorted_projects[i][0] <= curr_cap:
                heapq.heappush(heap, (-sorted_projects[i][1]))
                i += 1

            if not heap:
                break
            
            curr_cap += -heapq.heappop(heap) # add the capital from the current project

        return curr_cap
