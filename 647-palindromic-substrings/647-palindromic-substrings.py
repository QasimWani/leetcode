class Solution:
    def countSubstrings(self, s: str) -> int:
        # this is a generalized solution to max palindrome substring.
        # essentially, keep track of all palindromes you find along the way. base case: the set of characters in s are all palindromes.
        num_palindrome = 0
        
        for i in range(len(s)):
            # odd position
            counter_odd = self.palindrome(s, i, i)
            # even position
            counter_even = self.palindrome(s, i, i + 1)
            num_palindrome += counter_odd + counter_even
        return num_palindrome
    
    def palindrome(self, s, left_idx, right_idx):
        counter = 0
        
        while left_idx >= 0 and right_idx < len(s) and s[left_idx] == s[right_idx]:
            left_idx -= 1
            right_idx += 1
            counter += 1
        return counter
        
            
        