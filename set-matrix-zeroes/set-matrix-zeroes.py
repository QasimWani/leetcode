class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #so the idea is as follows, whenever you see a zero, set the first element in the row and column
        #with a zero. in the second pass, set all the elements in row, col with a zero to zero.
        #note, we have to handle the first row differently because we can lead to setting the entire
        #matrix to 0. 
        
        # Time: O(M x N)
        # Space: O(1)
        
        m, n = len(matrix), len(matrix[0])
        set_first_column = False
                
        for i in range(m):
            #check to see if we need to set the first column to 0 later
            if matrix[i][0] == 0:
                    set_first_column = True
            for j in range(1, n):
                if matrix[i][j] == 0:
                    #set first element in the row and column with 0.
                    matrix[i][0] = 0 #set column to 0
                    matrix[0][j] = 0 #set row to 0
        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        #taking care of first row
        if matrix[0][0] == 0:
            matrix[0] = [0]*n

        
        #taking care of first column
        if set_first_column:
            for i in range(m):
                matrix[i][0] = 0
                