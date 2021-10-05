class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # since the substring will be a contigious set of characters, each time a character is repeated from a previous set of characters, the entire set will be void and will need to rebuild the unique character set.
        # can solve this simply using a table and keep track of unique characters. if a characters occurs more than once in the linear pass, then we rebuild the table and record the length of that.
        # we do this until the end and retrieve the maximum length of the table during the process.
        
        # Time: O(n^2)
        # Space: O(n) - worst case
        max_length = 0
        for i in range(len(s)):
            table = {}
            for j in range(i, len(s)):
                # given s[i], what's the maximum unique subarray you can build?
                if s[j] not in table:
                    table[s[j]] = True
                else:
                    break
                max_length = max(max_length, len(table))
        return max_length

                
            
                
                