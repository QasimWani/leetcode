class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        #basically merge intervals. if we can merge any intervals, then return false. else true.
        #in other words, if there exists another start between a start and an end, return false.
        #Time: O(n log n), where n is the number of intervals
        #Space: O(1)
        if not intervals:
            return True

        intervals.sort()
        start, end = intervals[0]
        
        for i in range(1, len(intervals)):
            if intervals[i][0] < end:#overlap found
                return False
            start, end = intervals[i]
        return True