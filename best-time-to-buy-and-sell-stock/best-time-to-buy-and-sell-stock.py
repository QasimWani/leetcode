# Time: O(n)
# Space: O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # essentially find min and max prices and calculate net profit.
        min_price, max_price = prices[0], float('-inf')
        current_delta = 0
        for x in prices[1:]:
            if min_price > x:
                min_price = x # buy at this point.
                max_price = float('-inf') # reset max price
            elif max_price < x and (max_price >= min_price or max_price == float('-inf')):
                max_price = x
                current_delta = max(current_delta, max_price - min_price)
        return max(0, current_delta)