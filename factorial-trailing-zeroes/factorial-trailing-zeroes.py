class Solution:
    def trailingZeroes(self, n: int) -> int:
        #O(n) solution is to compute the factorial and find the number of
        #trailing zeros.
        
        #Time: O(n)
        #Space: O(n!) ~ O(n^2)
        
        if n < 1:
            return 0
        #start from 1 factorial
        i = 1
        factorial = 1
        while i <= n:
            factorial *= i
            i += 1
        
        factorial = str(factorial)
        num_zeros = 0
        for i in range(len(factorial) - 1, -1, -1):
            if factorial[i] == '0':
                num_zeros += 1
            else:
                return num_zeros
        return num_zeros
        