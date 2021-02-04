class Solution:
    def countVowelStrings(self, n: int) -> int:
        # s[i - 1] <= s[i]
        # simple DP problem.
        # no need to additional auxillary memory because it seems to be deterministic
        
        dp = [1]*5
        for i in range(1, n):
            for j in range(len(dp)):
                dp[j] = sum(dp[j:])
        return sum(dp)
            