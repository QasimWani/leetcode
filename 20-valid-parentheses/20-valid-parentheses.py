class Solution:
    def isValid(self, s: str) -> bool:
        #Time: O(n)
        #Space: O(n), worst case (i.e. all opening characters)
        
        stack = []
        opening_dict = "[({"
        closing_dict = "])}"
        table = {"(" : ")", "{" : "}", "[" : "]"}
        
        for char in s:
            if char in opening_dict: # append to stack
                stack.append(char)
            if char in closing_dict: # pop from stack
                if len(stack) == 0: # going to pop from empty list.
                    return False
                pop = stack.pop()
                if table[pop] != char: # match!
                    return False
        return len(stack) == 0
            
                