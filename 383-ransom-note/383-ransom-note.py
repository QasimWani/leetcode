# Test –– sourced from: https://github.com/siddhantmedar/LeetCode/tree/main/383-ransom-note

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mp = {}
        
        for c in ransomNote:
            mp[c] = 1+mp.get(c,0)
            
        for c in magazine:
            if c in mp:
                mp[c]-=1
                
                if mp[c] == 0:
                    del mp[c]
                    
        return True if not mp else False