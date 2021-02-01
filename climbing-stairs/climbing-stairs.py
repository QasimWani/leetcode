#Time: O(n)
#Space: O(n)
        
class Solution:
    def climbStairs(self, n: int) -> int:
        #standard DP problem. n step depends on the reuslt of n - 1 step and so on and so forth.
        #the pattern also matches the Fibonacci sequence, because of 1 and 2 continuated steps.
        
        if(n <= 2):
            return n
        
        dp = [0]*n
        
        dp[0] = 1 #only 1 step to reach first step
        dp[1] = 2 #only 2 steps to reach second step
        
        for i in range(2, n):
            dp[i] = dp[i - 2] + dp[i - 1]
        return dp[-1]