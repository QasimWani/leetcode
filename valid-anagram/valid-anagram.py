class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Time:O(n + m), where n = len(s) and m = len(t)
        #Space: O(n + m)
        if len(s) != len(t):
            return False
        
        s_, t_ = {}, {}
        for char in s:
            s_[char] = s_[char] + 1 if char in s_ else 1

        for char in t:
            t_[char] = t_[char] + 1 if char in t_ else 1
            
        
        for char in s_:
            if not char in t_ or not t_[char] == s_[char]:
                return False
            
        return True