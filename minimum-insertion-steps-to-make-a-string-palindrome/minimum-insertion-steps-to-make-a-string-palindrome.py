class Solution:
    def minInsertions(self, s: str) -> int:
        #2 pointer approach where we check to see if s[left] = s[right]. if not, we insert the s[left] to s[right + 1].
        #we decrement right while it's greater than left as the bounding condition. after each iteration, we'll have a
        #character somewhere > left such that s[left] = s[new_position]. after this, we'll increment left by 1 until it
        #has traversed half of the original array. the max characters equals len(s)//2. so the answer is always less than
        #or equal to it.
        
        #Time: O(n), right pointer moves at most n^2 times while left pointer moves at most n/2 times.
        #Space: O(1)

#         s = list(s) #typecast to list for insertion
        
#         left, right = 0, len(s) - 1
#         n = len(s) #max swaps

#         count = 0
        
#         while left < right:
#             if s[left] != s[right]:
#                 # s.insert(right + 1, s[left])
#                 count += 1
#             else:
#                 right -= 1
#             left += 1
#             # print(s)
#         # print(s == s[::-1])
#         return count
    
            n=len(s)
            dp=[[0]*(n+1) for _ in range(n+1)]
            for i in range(n, -1, -1):
                print(i)
                for j in range(n):
                    if i<j:
                        dp[i][j]=dp[i+1][j-1] if s[i]==s[j] else 1+min(dp[i+1][j],dp[i][j-1])
            return dp[0][n-1]
        