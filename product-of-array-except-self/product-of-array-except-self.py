class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # create two arrays, prefix and suffix, of length num where prefix represents the product of all number to the left of number x and suffix represents the product to the right of x.
        # the answer at element i will be the product of predix_i and suffix_i.
        
        # Time: O(n)
        # Space: O(1)
        
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        
        for i in range(1, len(nums)):
            prefix[i] = nums[i - 1] * prefix[i - 1] 
        
        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = nums[i + 1] * suffix[i + 1] 

        return [prefix[i] * suffix[i] for i in range(len(nums))]
        