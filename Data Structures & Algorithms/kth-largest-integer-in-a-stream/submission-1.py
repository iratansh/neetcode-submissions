class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # have a min heap of size k
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)

        while len(self.heap) > self.k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        # three cases:
        # len(self.heap) < k: just add the num to the heap
        # len(self.heap) >= k: compare vals with heap[0] 
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        else:
            min_larg = self.heap[0]
            if val > min_larg:
                heapq.heappop(self.heap)
                heapq.heappush(self.heap, val)
        return self.heap[0]
