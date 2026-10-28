class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # an interval is overlapping if it starts before or at the prev interval end point
        intervals.sort()
        res = [intervals[0]]

        for i in range(1, len(intervals)):
            ps, pe = res[-1]
            s, e = intervals[i]

            if s <= pe:
                res[-1][0], res[-1][1] = min(ps, s), max(pe, e)
            else:
                res.append([s, e])
        return res
                

