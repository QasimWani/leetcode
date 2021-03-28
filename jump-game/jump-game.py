class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #Time: O(n)
        #Space: O(n)
        
        dp = [0]*len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1], nums[i - 1]) - 1
            if dp[i] < 0:#no possible way to continue
                return False
        return dp[-1] >= 0