# Time: O(n)
# Space: O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # essentially find min and max prices and calculate net profit.
        min_price, max_price = prices[0], float('-inf')
        current_delta = 0
        for x in prices[1:]:
            if x < min_price: # time to buy!
                min_price = x
                max_price = float('-inf')
            elif x > max_price:
                max_price = max(max_price, x)
                current_delta = max(current_delta, max_price - min_price)
        return max(0, current_delta)
                