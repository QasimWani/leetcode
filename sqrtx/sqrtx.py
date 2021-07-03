class Solution:
    def mySqrt(self, x: int) -> int:
        # simple binary search from 2 - x / 2
        if x < 2:
            return x
        left, right = 2, x // 2

        while left <= right:
            pivot = left + (right - left) // 2 # get midpoint number
            if pivot * pivot == x:
                return pivot
            if x >= pivot * pivot: #need to increase number
                left = pivot + 1
            else: # need to decrease number
                right = pivot - 1
        return right