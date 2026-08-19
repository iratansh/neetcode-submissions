class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # given n tasks where tasks[i] = [enqueue time, processing time]
        # only one task to process at a time
        # if cpu is idle there are avialble tasks: cpu choose task based off shortest processing time
        # min heap
        for i, task in enumerate(tasks):
            task.append(i)
        tasks.sort(key=lambda x:x[0])

        res, heap = [], [] # heap stores available tasks
        i, time = 0, tasks[0][0]

        while heap or i < len(tasks):
            # push all tasks with enqueue time <= current time to heap
            while i < len(tasks) and tasks[i][0] <= time:
                heapq.heappush(heap, (tasks[i][1], tasks[i][2])) # (processing_time, idx)
                i += 1
            
            if not heap:
                time = tasks[i][0]
            else:
                processing_time, task_idx = heapq.heappop(heap)
                time += processing_time
                res.append(task_idx)
        return res

