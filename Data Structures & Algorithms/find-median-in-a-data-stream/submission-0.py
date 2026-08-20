class MedianFinder:

    def __init__(self):
        self.min_h = [] 
        self.max_h = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_h, -num)
        heapq.heappush(self.min_h, -heapq.heappop(self.max_h))

        if len(self.max_h) + 1 < len(self.min_h):
            heapq.heappush(self.max_h, -heapq.heappop(self.min_h))
 
    def findMedian(self) -> float:
        if len(self.min_h) > len(self.max_h):
            return self.min_h[0]
        return (-self.max_h[0] + self.min_h[0]) / 2