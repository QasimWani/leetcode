class Solution:
    def isValid(self, s: str) -> bool:
        #Time: O(n)
        #Space: O(n), worst case (i.e. all opening characters)
        
        stack = []
        opening_char = "({["
        closing_char = ")}]"
        for num in s:
            if(num in opening_char):#push to stack
                stack.append(num)
            elif(num in closing_char):#pop and check
                if(not stack):
                    return False
                check = stack.pop()
                if(abs(ord(num) - ord(check)) > 2):#invalid
                    return False

        return len(stack) == 0