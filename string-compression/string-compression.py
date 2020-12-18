class Solution:
    def compress(self, chars: List[str]) -> int:
        #either this is the dumbest question i've seen, or i'm missing the point.
        #but basically, this is like run-length encoding except now instead of breaking characters of length > 9, it's continuous
        #and we're returning the length of encoded string.
        
        
        #Worst-case: time ==> O(n)
        #Space: O(1)
        
        
        if(len(chars) == 1): #only 1 character
            return 1
        
        
        
        N = len(chars)
        
        chars.append( [chars[0], 1] )
        
        count = 1
        for i in range(1, N):
            if(chars[i - 1] == chars[i]):
                count += 1
                chars[-1][1] = count  
            else:
                count = 1
                chars.append( [ chars[i], count ] )
            
        print(chars)
        print(N, len(chars))
        j = 0
        new_N = len(chars)
        for i in range(N, new_N):
            char, counter = chars[i][0], str(chars[i][1])
            chars.append(char)
            temp = 0
            while(int(counter) > 1 and temp != len(counter)):            
                chars.append(counter[temp])
                temp += 1
            
            
        chars[:new_N] = []
​
                
            
