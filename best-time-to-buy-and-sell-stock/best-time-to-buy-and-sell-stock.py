class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #basically find max peak in array.
        min_price = float('inf')
        max_profit = 0
        for num in prices:
            if num < min_price:
                min_price = num
            elif num - min_price > max_profit:
                max_profit = num - min_price
        return max_profit