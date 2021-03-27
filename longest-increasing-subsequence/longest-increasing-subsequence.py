class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #DP solution.
        #Time: O(n^2)
        #Space: O(n)
        
        dp = [0]*len(nums)
        dp[0] = 1
        global_max = 1
        for i in range(1, len(nums)):
            max_val = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    max_val = max(max_val, dp[j])
                    
            dp[i] = max_val + 1
            global_max = max(global_max, dp[i])
        return global_max
                
                
        