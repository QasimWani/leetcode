class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # O(n^2) solution would be setting a start index and while each character only appears once, keep moving the end character by one.
        
        start = 0
        table = set()
        end = start
        max_len = 0
        while start < len(s):
            if end == len(s) or s[end] in table: # non-unique character found. move start by one.
                start += 1
                end = start
                table = set() # reset table
            else:
                table.add(s[end])
                end += 1
            max_len = max(max_len, len(table))
        return max_len
        