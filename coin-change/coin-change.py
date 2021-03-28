class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #Time: O(m x n) where m is the amount and n is the number of coins
        #Space: O(m)
        dp = [float(1e10)]*(amount + 1)
        dp[0] = 0
        
        for coin in coins:
            for i in range(len(dp)):
                if i >= coin:
                    dp[i] = min(1 + dp[i - coin], dp[i])
        return dp[-1] if dp[-1] < float(1e10) else -1
                    
        