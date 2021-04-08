class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        #add up individual characters and take in the carry.
        #Time: O(max(n, m)) where n and m are the lengths of the strings a and b, respectively.
        #Space: O(max(n, m))
        
        if len(num1) < len(num2):
            num1, num2 = num2, num1
        
        result = ''
        carry = 0
        
        for i in range(1, len(num1) + 1):
            i *= -1
            
            a = int(num1[i])
            b = 0
            if abs(i) <= len(num2):
                b = int(num2[i])
                
            sum = a + b + carry
            carry = sum // 10
            result += str(sum % 10)

        if carry:
            result += str(carry)
        return result[::-1]
            
        