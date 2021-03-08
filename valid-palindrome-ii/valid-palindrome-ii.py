class Solution:
    def validPalindrome(self, s: str) -> bool:
        #use 2 pointers.
        #Time: O(n), where n = len(s)
        #Space: O(1)
        
        left, right = 0, len(s) - 1
        
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                remove_left = s[:left] + s[left + 1:]
                remove_right = s[:right] + s[right + 1:]
                return remove_left == remove_left[::-1] or remove_right == remove_right[::-1]
                
        return True
                
        