class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        #this is basically sorting an array except now we're keeping track of the number of
        #elements moved from their original position.
        #in the case of the array [1, 1, 4, 2, 1, 3], we swap 4 and 1 making it 2 elements moved.
        #this results in [1, 1, 1, 2, 4, 3], we swap 4 and 3 making it 1 unique element moved.
        #note that we already moved 4 before. This results it a total of 3 swaps.
        
        #Time: O(n log n) quick sort
        #Space: O(n) keeping track of elements moved.
        
        heap = heights.copy()
        heapq.heapify(heap)
        swaps = 0
        for i, x in enumerate(heights):
            x_h = heapq.heappop(heap)
            if x != x_h:
                swaps += 1
        return swaps