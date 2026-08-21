class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # max heap: stores (-prof)
        # sort by capital
        n = len(profits)
        sorted_proj = [[capital[i], profits[i]] for i in range(n)]
        sorted_proj.sort(key=lambda x:x[0]) 

        curr_cap = w
        heap = [] # max heap
        i = 0 # index in sorted_proj
        for _ in range(k):
            # start by appending all available projects to the max heap
            while i < n and sorted_proj[i][0] <= curr_cap:
                heapq.heappush(heap, -sorted_proj[i][1])
                i += 1
            
            # if max heap is empty we can break since no projects fit our budget
            if not heap:
                break

            # pop from the max heap
            curr_cap += -heapq.heappop(heap)
        
        return curr_cap