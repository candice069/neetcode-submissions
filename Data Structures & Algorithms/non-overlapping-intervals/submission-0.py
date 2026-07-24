class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])

        prev_end = intervals[0][1]#优先保留end时间较早的区间
        removed = 0

        for start, end in intervals[1:]:
            if start < prev_end:
                removed += 1
            else:
                prev_end = end
        return removed