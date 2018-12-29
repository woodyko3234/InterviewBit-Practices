# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(self, intervals):
        #not sorted yet
        #sort first
        if len(intervals) == 0: return []
        interval_len = len(intervals)
        intervals.sort(key = lambda k: k.start)

        i = 1
        while i < len(intervals):
            if i >= 1 and intervals[i].start <= intervals[i-1].end:
                intervals[i].start = intervals[i-1].start
                if intervals[i].end < intervals[i-1].end:
                    intervals[i].end = intervals[i-1].end
                intervals.pop(i-1)
            else: i += 1
        return intervals
