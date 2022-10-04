class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # O(n) solution would be setting a start index and while each character only appears once, keep moving the end character by one.
        
        table = [-1] * 128
        max_len = 0
        start = -1
        
        for i, char in enumerate(s):
            ascii = ord(char) # get ascii value of character
            if table[ascii] > start: # character found at least once in substring
                start = table[ascii]
            table[ascii] = i # store current position in character map
            max_len = max(max_len, i - start)
        return max_len
# LeetHub test...