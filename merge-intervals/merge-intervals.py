class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        starts, ends = zip(*intervals)
        #sort the intervals by start indices
        indices = [i[0] for i in sorted(enumerate(starts), key=lambda x:x[1])]
        
        start, end = starts[indices[0]], ends[indices[0]] #cache first interval
        
        result = []
        
        for i in range(1, len(starts)):
            if end >= starts[indices[i]]:
                if end >= ends[indices[i]]:
                    continue
                end = ends[indices[i]]
            else:
                result.append([start, end])
                start, end = starts[indices[i]], ends[indices[i]]
            
        return result + [[start, end]]
                
            
        