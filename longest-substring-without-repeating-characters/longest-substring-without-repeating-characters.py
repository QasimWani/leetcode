class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #this can be solved using the sliding window solution. Basically, we need to maintain a counter of character occurances
        #in a two-pointer interval. As long as each character in the interval occurs just once, we're fine. If we get a character that
        #occurs more than once in the current interval, we increment the left pointer. Otherwise, we keep iterating the right pointer.
        #While doing so, we'll be storing the max value so at any i-j value, we are guaranteed to have the max subarray problem solved.
        
        # Time: O(n)
        # Space: O(1)
        
        table = [-1]*256
        
        if(len(s) <= 1):
            return len(s)
        
        max_length = 0
        start = -1
        
        for i in range(len(s)):
            asc = ord(s[i])
            if(table[asc] > start):#set new bound
                start = table[asc]
            table[asc] = i
            max_length = max(max_length, i - start)
            
        return max_length
            
            
                    
                
                