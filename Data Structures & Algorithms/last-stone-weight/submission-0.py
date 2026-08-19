class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # stones[i] represents the weight of the ith stone
        # each step take the two heaviest stones and do the simulation
        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            s1, s2 = -heapq.heappop(heap), -heapq.heappop(heap)
 
            if s1 > s2:
                s1 = s1 - s2
                heapq.heappush(heap, -s1)

        return -heap[0] if heap else 0
        