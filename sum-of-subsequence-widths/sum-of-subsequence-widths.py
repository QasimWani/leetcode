class Solution:
    def sumSubseqWidths(self, A: List[int]) -> int:
        ### Solve using powersets and have the first element as min and last element as max.
        ### min-max can be established as 1st - last elment if input array is sorted, which can be done in-place.
        A.sort()
        M = 10**9 + 7
        P = [(2**i)%M for i in range(len(A))]
        res = 0
        for i in range(len(A)):
            add = P[i] * A[i]
            ded = P[len(A)-1-i]* A[i]
            res = (res + (add - ded) ) % M
        return res