class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        #Whenever there exists an overlap, we need to book an additional room. The idea is to use a priority queue where the priority is based on its starting time.
        #if the current element's starting time is greater than the min heap's starting time, we pop it and push in the with new end time.
        
        #Time: O(n log n)
        #Space: O(n)
        
        intervals.sort()
        merge = []
        heapq.heappush(merge, intervals[0][1]) #push elements based on their end time as priority
        
        for i in range(1, len(intervals)):
            if merge[0] <= intervals[i][0]: #overlap found. pop element from heap
                heapq.heappop(merge)
            heapq.heappush(merge, intervals[i][1])
        return len(merge)