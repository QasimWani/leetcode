class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        #perform BFS on each 1 in the matrix
        m, n = len(matrix), len(matrix[0])
        self.updated_board = [[0]*n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    self.bfs(matrix, i, j)
                    
        return self.updated_board
        
    
    def bfs(self, grid, pos_x, pos_y):
        queue = [(pos_x, pos_y)]
        depth = 0
        while queue:
            for _ in range(len(queue)):
                x, y = queue.pop(0)
                if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
                    if grid[x][y] == 0:
                        self.updated_board[pos_x][pos_y] = depth
                        return
                    queue.append((x + 1, y))
                    queue.append((x - 1, y))
                    queue.append((x, y + 1))
                    queue.append((x, y - 1))
                    
            depth += 1
                
        return
        
        