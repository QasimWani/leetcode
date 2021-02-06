class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0]*(len(s) + 1)
        dp[0] = 1 #empty char
        for i in range(1, len(dp)):
            single = int(s[i - 1])
            double = int(s[i - 2] + s[i - 1]) if i - 2 >= 0 else 0
            
            if(1 <= single <= 9):
                dp[i] += dp[i - 1]
            if(10 <= double <= 26):
                dp[i] += dp[i - 2]
                
        return dp[-1]