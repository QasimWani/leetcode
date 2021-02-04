class Solution:
    def countVowelStrings(self, n: int) -> int:
        
        dp = [1] * 5
        
        for i in range(1, n):
            for j in range(len(dp)):
                dp[j] = sum(dp[j:]) #takes care of the lexicographical order
        
        return sum(dp) #return the sum of indiviaul instances of all characters with length n.