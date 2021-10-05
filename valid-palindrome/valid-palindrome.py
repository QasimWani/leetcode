import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 2 pointer approach. keep iterating inwards, left and right should point to the same character.
        # Time: O(n)
        # Space: O(1)
        
        s = re.sub(r'[^A-Za-z0-9 \t]+', '', "".join(s.split(" "))).lower()
        left, right = 0, len(s) - 1

        while left < right: # middle character or open pivot. doesn't matter which one it is :D
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True