class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = []
        
    def push(self, x: int) -> None:
        self.stack.append(x)
        self.min.append( min(self.min[-1] if self.min else float('inf'), x) )

    def pop(self) -> None:
        self.stack.pop(-1) #LIFO
        self.min.pop(-1) #LIFO

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