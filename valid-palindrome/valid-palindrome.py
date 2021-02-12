class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [char.lower() for char in s if char.isalnum()]
        half = len(s)//2
        return s[:half] == s[::-1][:half]