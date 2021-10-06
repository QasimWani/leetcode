class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        # sliding window solution. starting from index i, how many indices i + j can you go up to such that the total number of unique characters between s[i : j + 1] ≤ k?
        
        # Time: O(n)
        # Space: O(k)
        if k == 0:
            return 0
        
        max_length = 0
        left, right = 0, 0
        
        table = {}
        while right < len(s):
            table[s[right]] = right # gather latest position of character
            right += 1
            if len(table) > k: # retrieve position of most recent character and pop it
                lrp = min(table.values())
                del table[s[lrp]]
                left = lrp + 1
            
            max_length = max(max_length, right - left)
            
        return max_length