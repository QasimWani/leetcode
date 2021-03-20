class Solution:
    def addBinary(self, a: str, b: str) -> str:
        #Time: O(max(n, m)) where n and m are the lengths of the strings a and b, respectively.
        #Space: O(max(n, m))
        
        if len(a) < len(b):
            a,b = b, a #making sure a >= b
        
        n = len(a)
        output = ''
        carry = 0
        
        for i in range(1, n + 1):
            i *= -1
            sum = int(a[i]) + int(b[i]) + carry if abs(i) <= len(b) else int(a[i]) + carry
            carry = 0
            if sum > 1:
                carry = 1
                
            sum %= 2
            output += str(sum)
        if carry:
            output += str(carry)
            
        return output[::-1]