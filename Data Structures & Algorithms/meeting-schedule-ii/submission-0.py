"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0:
            return 0
        intervals.sort(key=lambda x: (x.start, x.end))
        ends = [intervals[0].end]

        for i in range(1, len(intervals)):
            added = False
            for j, end in enumerate(ends):
                if end <= intervals[i].start:
                    ends[j] = intervals[i].end
                    added = True
                    break
            
            if not added:
                ends.append(intervals[i].end)
        
        return len(ends)
                    
