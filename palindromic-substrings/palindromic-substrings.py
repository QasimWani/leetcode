class Solution:
    def countSubstrings(self, s: str) -> int:
        # naive algorithm. generate all possible substrings and check if that substring is a palindrome or not. the time complexity for this would be O(n^3)
        # efficient pruning will be to look at previous substring. if previous substring is not a palindrome, will the addition of new character make it a palindrome?
        # now that i think about it, the best way to solve it is by finding maximum length palindrome. if we find a max palindromic substring, we effectively have searched for all possible contiguous palindromes.
        # instead of returning max palindrome, we just add each new palindrome we find to a dictionary.
        
        # Time : O(n^2)
        # Space: O(1)
        
        result = 0
        
        for center in range(len(s)):
            i, j = center, center # starting at character
            while i >= 0 and j < len(s) and s[i] == s[j]:
                result += 1
                i -= 1
                j += 1
            
            i, j = center, center + 1 # starting at pivot
            while i >= 0 and j < len(s) and s[i] == s[j]:
                result += 1
                i -= 1
                j += 1
        return result
            