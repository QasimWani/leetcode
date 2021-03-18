class MyQueue:
    """FIFO Architecture"""
    def __init__(self):
        """
        Initialize your data structure here.
        """
        #All operations take O(1) amortized time to complete.
        
        self.top = -1
        self.arr = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.arr.append(x)
        self.top = self.arr[0]

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        del self.arr[0]
        top = self.top
        self.top = self.arr[0] if not self.empty() else -1
        return top

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.top

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.arr) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()