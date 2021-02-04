class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #we can build a frequency counter for all elements, and pass it through a heap. 
        #when we pop each element from a heap, it will return the value that is of greatest frequency. 
        #Time: O(n log k)
        #Space:O(n + k)
        set = {}
        for num in nums:
            if(num in set):
                set[num] += 1
            else:
                set[num] = 1
        heap = [(freq, num) for num, freq in list(set.items())]
        
        heapq.heapify(heap)
        for _ in range(len(set) - k):
            heapq.heappop(heap)[1] 
        return [num[1] for num in heap]