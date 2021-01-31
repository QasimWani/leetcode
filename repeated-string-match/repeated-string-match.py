class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        #we first need to repeat a enough times until len(a) > len(b).
        #after doing that, we have to check if a repeated to itself at most 2 times gives b as substring. if not, return -1.
        
        #to repeat a until len(a) >= len(b), we can simply do a * len(a)/len(b)    
        k = ceil(len(b)/len(a))
        
        for i in range(2):
            if(b in a * (k + i)):
                return k + i
        
        return -1