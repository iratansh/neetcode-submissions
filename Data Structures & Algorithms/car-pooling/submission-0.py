class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # pick up the passengers closest to the current point?
        # if we arrive at a location where we must pick up passengers but there is not enough capacity left we must return False
        # need to track capacity as we go through the trips
        trips.sort(key=lambda x:x[1])
        heap = []
        passenger = 0

        for npass, s, e in trips:
            # while there are elemnts in the heap and the end time of the trips is at or before the current time
            while heap and heap[0][0] <= s:
                passenger -= heapq.heappop(heap)[1] 

            heapq.heappush(heap, (e, npass))
            passenger += npass

            if passenger > capacity:
                return False
        return True




        

