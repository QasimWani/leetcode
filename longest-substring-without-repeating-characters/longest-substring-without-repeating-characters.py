class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # since the substring will be a contigious set of characters, each time a character is repeated from a previous set of characters, the entire set will be void and will need to rebuild the unique character set.
        # this can be solved by keeping track of two pointers, sort of. Each time we move to a new unique character, we move the right pointer by one. And each time we see a character we've already seen, we move the left
        # pointer to the right until the set of characters between left and right pointers are all unique. We don't have to do a second traversal in the sliding window approach. Since the input is guaranteed to be the set
        # of all characters, we can create a character array of size 256. And each time we enter we enter a new value we assign the unicode value of that character by the current index. And if we see that we've already
        # traversed through that character, we reset its value with the current index.
        
        # Time: O(n)
        # Space: O(1)
        
        table = [-1] * 256
        start = -1
        max_length = 0
        for i, char in enumerate(s):
            asc = ord(char) # get unicode value
            if table[asc] > start: # we've seen this value before
                start = table[asc] # reset bound with that value
            table[asc] = i
            max_length = max(max_length, i - start)
        return max_length