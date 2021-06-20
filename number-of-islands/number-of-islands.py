class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #the idea is to perform DFS starting from the first instance of '1' in the array.
        #from there we perform DFS on each node until both the right and down cell are 0 or are at the edge. For every '1' we see, we replace it with an 'x'
        #to indicate that we've traversed over that node. Once we return from traversing all nodes of the first cell with '1' we'll now have an updated map
        #of all elements in the grid with an 'x' where the first island was supposed to be. We now continue the process until we find the next '1' in the grid.
        #We can optimize the solution by using memoization and caching in our nodes but either way, this is the optimal solution in terms of time complexity.
        
        #Time: O(m x n)
        #Space: O(m x n)
        
        m, n = len(grid), len(grid[0])
        counter = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1': #start DFS
                    self.dfs(grid, i, j)
                    counter += 1
        return counter
    
    def dfs(self, grid, x, y):
        if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == '1':
            grid[x][y] = 'x'
            self.dfs(grid, x + 1, y)
            self.dfs(grid, x - 1, y)
            self.dfs(grid, x, y + 1)
            self.dfs(grid, x, y - 1)
            
        return