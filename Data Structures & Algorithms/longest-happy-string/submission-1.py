class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # have a max heap to pick the char that appears the most
        # the same char is allowed back to back at most 2 times
        res = []
        heap = [(count, char) for count, char in [(-a, 'a'), (-b, 'b'), (-c, 'c')] if count < 0] # or count > 0 with positive check
        heapq.heapify(heap)

        while heap:
            cnt, char = heapq.heappop(heap)
            if len(res) >= 2 and char == res[-1] == res[-2]: # 3 in a row can't use the char
                if not heap: # heap is empty so its not possible to make a longer str
                    break
                cnt2, char2 = heapq.heappop(heap)
                res.append(char2)

                heapq.heappush(heap, (cnt, char)) # put back the original char
                if cnt2 + 1 < 0: 
                    heapq.heappush(heap, (cnt2 + 1, char2))
            else: # not possible to make 3 in a row
                res.append(char)
                if cnt + 1 < 0:
                    heapq.heappush(heap, (cnt + 1, char))

        return "".join(res) 