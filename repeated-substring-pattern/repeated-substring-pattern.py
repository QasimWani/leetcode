class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        #string rotation technique in O(n) time with O(1) space
        l = len(s)
        for i in range(1, l//2 + 1):
            if(l % i == 0 and s[0:l - i] == s[i:]):
                return True
        return False