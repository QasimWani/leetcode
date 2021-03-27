class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1
        start_num = False
        res = 0
        for char in s:
            if char == ' ':#whitespace, ignore
                if start_num:
                    break
                continue
            
            if char == '+' or char == '-':
                if start_num:
                    break
                
                start_num = True
                if char == '-':
                    sign = -1
                continue
            
            if char.isdigit():
                start_num = True
                res += int(char)
                res *= 10
            else:
                break
        res = sign * res // 10
        if sign == -1:#clamp res
            return max(res, -2**31)
        return min(res, 2**31 - 1)