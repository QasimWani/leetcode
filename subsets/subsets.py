class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = [[]]
        for num in nums:
            for i in range(len(subset)):
                val = subset[i] + [num]
                subset.append(val)
        return subset
        
