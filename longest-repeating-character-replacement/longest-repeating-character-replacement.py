from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # simple 2 pointer sliding window approach. given left and right pointers both starting at first index, move right pointer by one to the right until the set of characters between left and right
        # are no longer the same. Move left pointer by one, and continue the process. The idea is that you trynna set the right pointer value to left pointer.
        
        # Time: O(n)
        # Space: O(1)
        
        left = max_count = right = 0
        table = defaultdict(lambda : 0)
        result = 0
        while right < len(s):
            table[s[right]] += 1
            max_count = max(max_count, table[s[right]])
            if right - left + 1 > max_count + k: # reset
                table[s[left]] -= 1
                left += 1
            
            result = max(result, right - left + 1)
            right += 1
        return result