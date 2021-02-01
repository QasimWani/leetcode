#Time: O(n)
#Space: O(n)

class Solution:
    def rob(self, nums: List[int]) -> int:
        #using similar structure to Kadane's algorithm, except this time you cannot end with house[-1] and house[0] as max subarray
        #because array is cyclic.
        #To solve this, we need to come up with max-subarray starting from index = 0, and then with index = 1.
        #once solved those 2 independently, we return the maximum value. and that should be the final solution!
        
        if(len(nums) <= 2):
            return max(nums) if nums else 0
        
        dp = [0]*(len(nums) - 1)
        dp[0] = nums[0]
        dp[1] = max(dp[0], nums[1])
        
        for i in range(2, len(nums) - 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        
        max_0 = dp[-1]
        
        #find max with index = 1 as initial point
        dp[0] = nums[1]
        dp[1] = max(dp[0], nums[2])

        for i in range(3, len(nums)):
            dp[i - 1] = max(dp[i - 2], dp[i - 3] + nums[i])
            
        return max(max_0, dp[-1])