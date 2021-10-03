class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # at every index we need to make a descision, is this (the new element) the max subarray or will adding the new entry make the sum even bigger? This is done while keeping track of global sum.
        # time: O(n)
        # space: O(1)
        global_sum = local_sum = nums[0]
        
        for x in nums[1:]:
            local_sum = max(x, local_sum + x)
            global_sum = max(global_sum, local_sum)
        return global_sum