#Time: O(n^2)
#Space: O(n)

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #recursive approach with memoization, aka top-down approach
        #recursively checks if the first word in the dictionary is present
        #in the array s. If so, pop it out and recurse again until 
        #either the string is empty (return True) or done with recursion (return false)
        
        return self.helper(s, wordDict, {})
    
    def helper(self, s, dict, mem):
        if(len(s) == 0):
            return True
        elif(s in mem):
            return mem[s]
        
        for x in dict:
            if(s[:len(x)] == x and self.helper(s[len(x) : ], dict, mem)):
                mem[s] = True
                return True
            
        mem[s] = False
        return False