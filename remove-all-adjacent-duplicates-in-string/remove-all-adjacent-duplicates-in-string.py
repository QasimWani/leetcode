class Solution:
    def removeDuplicates(self, S: str, i=0) -> str:
        #solve using a stack in O(N) time and space.
        stack = []
        
        for char in S:
            if stack and stack[-1] == char:
                stack.pop(-1)
            else:
                stack.append(char)
        return "".join(stack)