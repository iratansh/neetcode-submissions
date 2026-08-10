class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # min heap approach: (dist, int)
        heap = []
        res = []

        for num in arr:
            dist = abs(num - x)
            heapq.heappush(heap, (dist, num))

        while len(res) < k:
            _, pnt = heapq.heappop(heap)
            res.append(pnt)
        res.sort()
        return res
