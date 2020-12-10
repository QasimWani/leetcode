class Solution:
    def numSplits(self, s: str) -> int:
        result = 0
        length = len(s)
        
        left_letters = [0]*26
        right_letters = [0]*26
              
        for i in range(length):
            right_letters[ord(s[i]) - ord('a')] += 1
        
        for i in range(length):
            right_letters[ord(s[i]) - ord('a')] -= 1
            left_letters[ord(s[i]) - ord('a')] += 1
            
            result += (right_letters.count(0) == left_letters.count(0))
        
        return result
        
