class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # two pointer sliding window approach.
        # Given a substring, can you make enough edits within the budget you have to convert it into a valid character replacement substring?
        # Time: O(n*26) = O(n)
        # Space: O(26) = O(1)
        
        start = end = 0
        table = collections.defaultdict(int)
        max_len = 0
        while end < len(s):
            table[s[end]] += 1
            # get the most frequent character count and see if you can make replacement on other characters
            cnt = self.getMaxFrequency(table)
            if end - start + 1 - cnt <= k: # can make replacement
                max_len = max(max_len, end - start + 1)
            else: # can't make a replacement, move start pointer by one.
                table[s[start]] -= 1
                start += 1
            end += 1
            
        return max_len
                
    
    def getMaxFrequency(self, table:dict):
        return max(table.values())