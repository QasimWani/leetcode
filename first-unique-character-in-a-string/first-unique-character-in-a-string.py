class Solution:
    def firstUniqChar(self, s: str) -> int:
        #Two pass algorithm. Space = O(1); Time = O(n)
        table = {}
        for i, char in enumerate(s):
            if char in table:
                table[char][0] += 1
            else:
                table[char] = [1, i]
        
        for x in table:
            if table[x][0] == 1:
                return table[x][1]
        return -1
