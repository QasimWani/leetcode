class Solution:
    def countBits(self, num: int) -> List[int]:
        #Suboptimal process: 
        #   for 0 ≤ i ≤ num:
        #       1. convert i to binary
        #       2. count number of ones.
        ### Time: O(n * sizeof(integer))
        ### Space: O(n * sizeof(integer))
        
        arr = []
        for i in range(num + 1):
            x = str(bin(i))
            arr.append(x.count('1'))
        
        return arr
            
        
