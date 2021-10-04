class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # since we're dealing with negative numbers and negative times negative can return large positive, we'd need to keep track of local min and max. Because you can be local min for now, but multiplying with next
        # number can easily turn you into max if negative.
        # example: [4, -2, -10]. answer should be the product of all numbers.
        
        # Time: O(N)
        # Space: O(1)
        
        local_min = local_max = nums[0]
        
        global_max = nums[0]
        
        for x in nums[1:]:
            temp_max = max(x, local_min * x, local_max * x)
            local_min = min(x, local_min * x, local_max * x)
            local_max = temp_max            
            
            global_max = max(global_max, local_max)
        return global_max
            