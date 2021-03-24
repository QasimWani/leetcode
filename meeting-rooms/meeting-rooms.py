class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        #basically merge intervals. if we can merge any intervals, then return false. else true.
        #in other words, if there exists another start between a start and an end, return false.
        #Time: O(n log n)
        #Space: O(n)
        if not intervals:
            return True
        
        starts, ends = zip(*intervals)
        indices = [i[0] for i in sorted(enumerate(starts), key=lambda x:x[1])] #sort the intervals by start indices
        
        start, end = intervals[indices[0]]
        
        for i in range(1, len(starts)):
            if starts[indices[i]] < end:#overlap found
                return False
            start, end = starts[indices[i]], ends[indices[i]]
        return True