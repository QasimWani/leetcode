class Solution:
    def longestPalindrome(self, string: str) -> str:
        # so, there are two cases for palindromes.
        # 1) palindrome across a pivot. e.g. [p x a x p]. Here, it's pivoted across a.
        # 2) palindrome across the center. e.g. [q b g g b q]. Here, the center is between the two g's.
        
        # we start at a character and expand outwards. while all the characters expanded outwardly are palindrome, keep expanding.
        substr = ""
        max_substr = ""
        for i in range(len(string)):
            # palindrome of odd length –– start from pivot [case 1]
            left, right = i, i
            while left >= 0 and right < len(string) and string[left] == string[right]:
                left -= 1
                right += 1
                
            substr = string[left+1 : right]
            if len(substr) > len(max_substr):
                max_substr = substr
            # palindrome of even length –– start between two characters
            left, right = i, i + 1
            while left >= 0 and right < len(string) and string[left] == string[right]:
                left -= 1
                right += 1
                
            substr = string[left+1 : right]
            if len(substr) > len(max_substr):
                max_substr = substr
        return max_substr