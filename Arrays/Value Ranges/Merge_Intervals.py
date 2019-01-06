# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
        start, end = newInterval.start, newInterval.end
        if len(intervals) == 0: return [newInterval]
        elif start >= intervals[-1].end: return intervals[:] + [newInterval]
        left, right = 0,0
        while right < len(intervals):
            if end <= intervals[right].start: break
            if start > intervals[right].end: left += 1
            else:
                start = min(start, intervals[right].start)
                end = max(end, intervals[right].end)
            right += 1
        return intervals[:left] + [Interval(start, end)] + intervals[right:]

'''
class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
        if len(intervals) == 0:
            return [newInterval]
        if newInterval.end < intervals[0].start:
            # Before intervals, no overlap
            return [newInterval] + intervals
        if newInterval.start > intervals[-1].end:
            # After intervals, no overlap
            return intervals + [newInterval]
        i = -1
        j = -1
        left = 0
        right = len(intervals)-1
        while left <= right:
            mid = left + (right-left)/2
            if intervals[mid].start < newInterval.start:
                left = mid
            elif intervals[mid].start > newInterval.start:
                right = mid
            else:
                i = mid
                break
            if mid == left + (right-left)/2:
                if intervals[right].start <= newInterval.start:
                    i = right
                break
        if i == -1:
            i = left
        left = 0
        right = len(intervals)-1
        while left <= right:
            mid = left + (right-left)/2
            if intervals[mid].start < newInterval.end:
                left = mid
            elif intervals[mid].start > newInterval.end:
                right = mid
            else:
                j = mid
                break
            if mid == left + (right-left)/2:
                if intervals[right].start <= newInterval.end:
                    j = right
                break
        if j == -1:
            j = left
        if i == j:
            # Check if they actually overlap or out of it
            if max(intervals[i].start,newInterval.start) > min(intervals[i].end,newInterval.end):
                # They don't overlap. We need to inject this interval
                return intervals[:i+1]+[newInterval]+intervals[i+1:]
        if max(intervals[i].start,newInterval.start) > min(intervals[i].end,newInterval.end):
            # Check if ith interval actually overlaps. It doesn't, so just increment
            i += 1
        if max(intervals[j].start,newInterval.start) > min(intervals[j].end,newInterval.end):
            # Check if jth interval actually overlaps. It doesn't, so just decrement
            j -= 1
        # i and j overlap
        leftEnd = min(intervals[i].start, newInterval.start)
        rightEnd = max(intervals[j].end, newInterval.end)
        newInterval = Interval(leftEnd, rightEnd)
        intervals = intervals[:i] + [newInterval] + intervals[j+1:]
        return intervals
'''
