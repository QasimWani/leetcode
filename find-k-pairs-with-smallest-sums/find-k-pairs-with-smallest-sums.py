class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        #O(n * m) solution.
        heap = []
        if max(len(nums1), len(nums2)) == 0:
            return []
        
        for i in nums1:
            for j in nums2:
                heap.append((i + j, [i, j]))
        
        heapq.heapify(heap)
        
        return [heapq.heappop(heap)[1] for _ in range(min(k, len(heap)))]