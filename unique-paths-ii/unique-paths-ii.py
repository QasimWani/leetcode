#Time = O(m * n); m = number of rows, n = number of columns
#Space = O(1), handling in-place.

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        #similar to Unique Paths I, except now we reset paths whenever we hit an obstacle.
        #DP algorithm: grid[i, j] = grid[i - 1, j] + grid[i, j - 1]
        #if obstacle, grid[i, j] = 0.
        
        if obstacleGrid[0][0] == 1: #no possible path possible
            return 0
        
        obstacleGrid[0][0] = 1 #set initial value
        
        row, col = len(obstacleGrid), len(obstacleGrid[0]) #get number of rows and columns
        
        for j in range(1, col): #set values of first row
            obstacleGrid[0][j] = obstacleGrid[0][j - 1] if obstacleGrid[0][j] == 0 else 0
        
        for i in range(1, row): #set values of first column
            obstacleGrid[i][0] = obstacleGrid[i - 1][0] if obstacleGrid[i][0] == 0 else 0
        
        #iterate remainder of grid
        for i in range(1, row):
            for j in range(1, col):
                obstacleGrid[i][j] = obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1] if obstacleGrid[i][j] == 0 else 0
        
        return obstacleGrid[-1][-1]