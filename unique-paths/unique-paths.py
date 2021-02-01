#Time : O(m * n), m = number of rows; n = number of columns
#Space: O(m * n), m = number of rows; n = number of columns
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #answer the question: how many ways can you reach a point i, j? Solving for subproblems can lead to final solution of m x n.
        #DP algorithm : grid[i,j] = grid[i-1,j] + grid[i,j-1]
        grid = [ [1 for _ in range(n)] for _ in range(m)]
        
        for r in range(1, m):
            for c in range(1, n):
                grid[r][c] = grid[r - 1][c] + grid[r][c - 1]
        
        return grid[-1][-1]