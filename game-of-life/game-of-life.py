import copy

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        #since we're supposed to return in-place, the first idea that comes in mind is to
        #use auxillary space as a base lookup for next state and then make modifications
        #on board parameter. That way, concurrent modifications don't alter the state of board
        #from there, it's just embedding the rules.
        #Time = Space = O(m * n).
        #The solution for Constant space is to have special code declaring what the previous
        #value of each cell was based on new update, i.e 2 represents previously dead & -1 
        #previously alive. 
        #After update, we reset all 2's to 1 and all -1 to 0.
        
        self.memory = copy.deepcopy(board)

        m, n = len(board), len(board[0]) #get dimensions
        
        #RULES
        #A. 1 -> 0, if less than 2 or more than 3 live neighbors
        #B. 1 -> 1, if 2 or 3 live neighbors
        #C. 0 -> 1, if exactly 3 live neighbors
        #D. 0 -> 0, if A, B, C are false.
        
        for i in range(m):
            for j in range(n):
                num_neighbors = self.getNeighbors(i, j)
                if(num_neighbors < 2 or num_neighbors > 3 and board[i][j] == 1):
                    board[i][j] = 0
                elif(num_neighbors == 3 and board[i][j] == 0):
                    board[i][j] = 1
        
    def getNeighbors(self, x, y):
        """Get number of live neigbor for cell = grid[x, y] with dimensions m and n"""
        
        m, n = len(self.memory) - 1, len(self.memory[0]) - 1 #get dimensions
        
        left = max(x - 1, 0)
        right = min(x + 1, m)
        up = max(y - 1, 0)
        down = min(y + 1, n)
        
        neighbors = 0
        for i in range(left, right + 1):
            for j in range(up, down + 1):
                if(self.memory[i][j] == 1):
                    if(x == i and y == j):
                        continue
                    neighbors += 1

        return neighbors