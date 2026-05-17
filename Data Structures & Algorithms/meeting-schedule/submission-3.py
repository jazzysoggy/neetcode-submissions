"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals = sorted(intervals, key=lambda s: (s.start, s.end))
        print([[i.start, i.end] for i in intervals])
        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[i - 1].end:
                return False
        
        return True

