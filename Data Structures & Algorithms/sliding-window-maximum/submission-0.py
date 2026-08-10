class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # use a queue to keep track of the max ints we've come across?
        # queue stores indices - montonically decreasing: q[nums[0]] > q[nums[1]] >...
        q = deque()
        res= []

        for r, num in enumerate(nums):
            # 1. Maintain monotonic property: pop smaller/equal values from the BACK
            while q and nums[q[-1]] <= num:
                q.pop()

            # 2. Add current index to the queue
            q.append(r)

            # 3. Evict indices that fall outside the left window bound [r - k + 1, r]
            if q[0] < r - k + 1:
                q.popleft()

            # 4. Only append to result once the window size reaches k
            if r >= k - 1:
                res.append(nums[q[0]])

        return res