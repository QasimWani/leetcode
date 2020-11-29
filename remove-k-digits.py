class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        #basically, remove all peak elements from num. The closer the peak is to the left-most number, the higher its wait.
        
        if(len(num) == k): #edge case for when len(num) = k
            return "0"
        
        if(k == 0): #nothing to remove, return as is.
            return num
        
        
        stack = list(num) #store base num
        stack.append('0')
        
        for _ in range(k):
            for i in range(len(stack) - 1):
                if(stack and stack[i] > stack[i + 1]): #peak found, pop it.
                    stack.pop(i)
                    break
​
        stack.pop()
        
        return str(int("".join(stack)))
                
        
        
        
