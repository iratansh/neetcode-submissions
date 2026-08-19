class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # return k closest points to (0, 0) 
        # min heap
        heap = []
        res = []

        for x, y in points:
            # calc x^2 + y^2 
            d = (x**2) + (y**2)
            heapq.heappush(heap, (d, x, y))
        
        while len(res) < k:
            _, x, y = heapq.heappop(heap)
            res.append([x, y])
        
        return res


