class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # an interval overlaps with another interval if its s < pe
        ns, ne = newInterval
        inserted = False
        res = []

        for i in range(len(intervals)):
            s, e = intervals[i]

            # before newinterval
            if e < ns:
                res.append([s, e])
            # overlap
            elif s <= ne:
                ns, ne = min(ns, s), max(ne, e)
            # after newInterval
            else:
                if not inserted:
                    res.append([ns, ne])
                    inserted = True
                res.append([s, e])

        if not inserted:
            res.append([ns, ne])
        return res