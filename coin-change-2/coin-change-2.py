# Time = O(n * m); n = amount, m = number of coins
# Space = O(n * m); n = amount, m = number of coins
​
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        #this seems to be a variation of Knapsack problem. Instead of having finite number of each coin,
        #we now have an infinite supply. Therefore, we need to modify the knapsack formulation a bit.
        #The way I worked around it is by instead of directly solving for the maximum number of ways
        #for target amount, we built up to that target starting from amount = 0. This DP based sub-problem
        #approach helps solve for target = amount effectively.
        #Using Knapsack approach, the value of each item is 1. the weight is defined by the coins list.
        #however, the optimization algorithm is as follows: v[i, j] = max(v[i-1,j], v[i-1,j] + v[i,j-coins[i - 1]])
        
        grid = [ [0]*(amount + 1) for _ in range(len(coins) + 1)]
​
        #augment first column of each row
        for i, _ in enumerate(grid):
            grid[i][0] = 1
        
        #run DP -> v[i, j] = max(v[i-1,j], v[i-1,j] + v[i,j-coins[i - 1]])
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                grid[i][j] = max(grid[i - 1][j], grid[i - 1][j] + grid[i][j - coins[i-1]] if j - coins[i-1] >= 0 else 0)
​
        return grid[-1][-1]
