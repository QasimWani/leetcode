class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        return B in len(A) * A if len(A) <= len(B) else False