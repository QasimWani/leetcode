class Solution:
    def minInsertions(self, s: str) -> int:
        #2 pointer approach where we check to see if s[left] = s[right]. if not, we insert the s[left] to s[right + 1].
        #we decrement right while it's greater than left as the bounding condition. after each iteration, we'll have a
        #character somewhere > left such that s[left] = s[new_position]. after this, we'll increment left by 1 until it
        #has traversed half of the original array. the max characters equals len(s)//2. so the answer is always less than
        #or equal to it.
        #note that since we can inset character at any index, at left, right we have 2 choices. insert at left, or insert at right.
        #the cost for doing so for left or right is the same, so in order to choose the one with least total cost, we make use of
        #memoization. This is where the DP solution comes into play.
        
        #Time: O(n^2), right pointer moves at most n^2 times while left pointer moves at most n/2 times.
        #Space: O(n)

        n = len(s)
        dp = [ [0]*(n + 1) for _ in range(n + 1) ]
        
            
        for left in range(n, -1, -1):
            for right in range(n):
                if left < right:
                    dp[left][right] = dp[left + 1][right - 1] if s[left] == s[right] else 1 + min( dp[left + 1][right], dp[left][right - 1] )
        
        return dp[0][n-1]
        