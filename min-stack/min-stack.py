class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        #Optimized stack structure. 
        #Time: O(1)
        #Space: O(n)
        
        self.stack = []
        self.min = []
        
    def push(self, x: int) -> None:
        self.stack.append(x)
        
        current_min = self.min[-1] if self.min else float('inf')
        if current_min >= x:
            self.min.append(x)
        

    def pop(self) -> None:
        popped_value = self.stack.pop(-1) #LIFO
        
        current_min = self.min[-1]
        
        if current_min == popped_value:#pop value
            self.min.pop(-1)


    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()