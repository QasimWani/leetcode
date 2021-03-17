class Solution:
    def countDigitOne(self, n):
        if n <= 0:
            return 0
        if 1 <= n <= 9:
            return 1
        head, level = n, 1
        while head > 9:
            level *= 10
            head //= 10
        if head == 1:
            return  self.countDigitOne(level-1) + self.countDigitOne(n-level) + n-level +1
        return (head) * self.countDigitOne(level-1) + self.countDigitOne(n-head*level) + level