class Solution:
    def reorganizeString(self, s: str) -> str:
        # max heap
        count = Counter(s)
        heap = []
        res = []
        prev = None # (val, key)

        for key, val in count.items():
            heapq.heappush(heap, (-val, key))
        
        while heap:
            val, key = heapq.heappop(heap)
            res.append(key)
            
            if prev is not None:
                heapq.heappush(heap, (prev[0], prev[1]))
                prev = None
            
            if val + 1 < 0:
                prev = (val + 1, key)


        return "".join(res) if len(res) == len(s) else ""