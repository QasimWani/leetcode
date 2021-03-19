class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #Time: O(n)
        #Space: O(n)
        
        nums = set(nums)
        for i in range(len(nums)):
            if i not in nums:
                return i
        return len(nums)