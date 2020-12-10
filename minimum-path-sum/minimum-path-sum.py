class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        #alright, so this is a simple DP problem. 
        #the way i solved this is by first creating a 2d grid of indices the grid. 
        #from there, every index of the grid is the min(grid[left], grid[top]). and that's pretty much it.
        #super simple solution.
        
        ###### Complexity ########
        # Time: O(m*n), where m = number of rows and n = number of columns
        # Space: O(m*n), where m = number of rows and n = number of columns
        
        m, n = len(grid), len(grid[0]) #get number of rows and columns, respectively
        
        # create mxn grid
        grid_indices = [ [0 for j in range(n)] for i in range(m) ]
        
        grid_indices[0][0] = grid[0][0] #set initial value
        
        #set values for first row
        for i in range(1, n):
            grid_indices[0][i] = grid[0][i] + grid_indices[0][ i - 1]
            
        #set values for first column
        for i in range(1, m):
            grid_indices[i][0] = grid[i][0] + grid_indices[ i - 1][0]
        
        
        ### iterate through remaining values
        for r in range(1, m):
            for c in range(1, n):
                grid_indices[r][c] = grid[r][c] + min(grid_indices[r - 1][c], grid_indices[r][c - 1])
            
        
        return grid_indices[-1][-1]
        
