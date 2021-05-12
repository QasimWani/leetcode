class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #Pretty straightforward solution - we first sort the array based on the indices of starting indices. If the start
        #times were already sorted, the solution would run in linear time. From observation, it overlaps if and only if
        #there exists a start between a previous start and end time. We make use of a start and end sliding pointer to 
        #keep track of this and accordingly append our array based on this property.
        
        #Time: O(n log n), where n is the number of intervals. 
        #Space: O(n) where n is the number of intervals
        
        starts, ends = zip(*intervals)
        indices = [i[0] for i in sorted(enumerate(starts), key=lambda x:x[1])] #sort the intervals by start indices
        
        start, end = starts[indices[0]], ends[indices[0]] #cache first interval
        
        result = []
        
        for i in range(1, len(starts)):
            if end >= starts[indices[i]]:
                #just because an end time is greater than the current start time doesn't mean that it's also greater than the current
                #end time. We have to check for this. An example of this is [ [1, 4], [2, 3] ]. Without the below condition, the 
                #output would've been [1, 3]. But the answer should be [1, 4]. Using this, we can elongate the end time and essentially
                #recompare on the next timestep.
                if end >= ends[indices[i]]:
                    continue
                end = ends[indices[i]]
            else:
                result.append([start, end])
                start, end = starts[indices[i]], ends[indices[i]]
            
            
        return result + [[start, end]]