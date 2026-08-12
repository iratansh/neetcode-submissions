class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # monotonic increasing stack? we are limited by the shortest height when calculating area?
        # 2 cases: we are at a square >= stack[-1]: can therefore recompute the max area
        # other case is sqare < stack[-1] in which case we have to start area calculations again starting from this position
        stack = []
        max_area = 0

        for i, h in enumerate(heights):
            start = i

            # shorter bar: pop the stack and recompute max area?
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                max_area = max(max_area, height * (i - idx))
                start = idx
            stack.append((start, h))

        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))
        return max_area
