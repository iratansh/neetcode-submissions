class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # monotonically increasing stack: stack stores indexes of temperatures
        res = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            # maintain monotonic property
            while stack and temperatures[stack[-1]] < temp:
                j = stack.pop()
                res[j] = i - j
            stack.append(i)
        return res

