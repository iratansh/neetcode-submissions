class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # have a q to store tasks in cooldown
        # have a heap to store available tasks: keep iterating until heap is empty and cooldown has elements?
        q = deque() # [-cnt, idletime]
        count = Counter(tasks)
        heap = [-cnt for cnt in count.values()]
        heapq.heapify(heap)
        time = 0

        while heap or q:
            time += 1

            if not heap:
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(heap)
                if cnt:
                    q.append([cnt, time + n])
            
            if q and q[0][1] == time:
                heapq.heappush(heap, q.popleft()[0])
        
        return time