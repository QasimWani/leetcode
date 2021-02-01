#Time = Space = O(n)
class Solution:
    def rob(self, nums: List[int]) -> int:
        #this is a standard max subarray problem that can be solved using kadane's algorithm
        if(len(nums) <= 2):
            return max(nums) if nums else 0
        
        dp = [0]*len(nums)
        
        dp[0] = nums[0]
        dp[1] = max(nums[1], dp[0])
        
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        
        return dp[-1]