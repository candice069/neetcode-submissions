"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        #next_meeting_start > last_end
        intervals.sort(key =lambda x: x.start)

        #use heap to record the end time of meetings
        prev_end = intervals[0].end
        for interval in intervals[1:]:
            if prev_end > interval.start:
                return False
            prev_end = interval.end
        return True
