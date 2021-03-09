class Solution:
    def countSubstrings(self, s: str) -> int:
        #basically a variation of max palindrome substring problem.
        #let's find the largest palindrome first. and then find the second largest palindrome, and so on...
        #until we hit the smallest character which is also a palindrome.
        
        #Time: O(N)
        #Space: O(1)
        
        #utility function
        def isPalindrome(string):
            return string == string[::-1]
        
        counter = 0
        
        level = 0
        
        while level < len(s):
            l, r = level, 0 #define left and right pointers
            while l >= 0:
                px = isPalindrome(s[l: len(s) - r])
                if px:
                    counter += 1
                l -= 1
                r += 1
            
            level += 1
                
        return counter