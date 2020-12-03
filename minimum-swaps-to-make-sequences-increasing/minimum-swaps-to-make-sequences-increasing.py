#Time: O(n)
#Space: O(m), where m is the length of A; technically O(2*m), one for swap and non-swap
class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        no_swap = [int(1e10)]*len(A)
        swap = [int(1e10)]*len(A)
        
        swap[0] = 1 #base case.
        no_swap[0] = 0 #base case.
        
        #iterate
        for i in range(1, len(A)):
            a1, a2 = A[i-1], A[i]
            b1, b2 = B[i-1], B[i]
            
            if(a2 > a1 and b2 > b1): #take previous swap values
                no_swap[i] = no_swap[i - 1]
                swap[i] = 1 + swap[i - 1]
            
            #perform cross comparison
            if(b2 > a1 and a2 > b1):
                no_swap[i] = min(no_swap[i], swap[i - 1])
                swap[i] = min(swap[i], 1 + no_swap[i - 1])
                
        return min(swap[-1], no_swap[-1])
