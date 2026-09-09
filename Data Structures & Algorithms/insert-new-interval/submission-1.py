class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        intervals.append(newInterval)
        intervals.sort(key = lambda x: x[0])

        for start, end in intervals:
            if not res or start > res[-1][1]:
                res.append([start, end])
            elif start <= res[-1][1]:
                res[-1][1]= max(end, res[-1][1])
        return res