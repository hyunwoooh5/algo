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

        intervals = [[e.start, e.end] for e in intervals]

        intervals.sort()

        prev_start, prev_end = intervals[0]

        for start, end in intervals[1:]:
            if prev_end <= start:
                prev_start, prev_end = start, end
            else:
                return False
        return True
