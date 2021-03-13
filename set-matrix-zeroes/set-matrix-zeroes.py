class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # two-pass, constant space solution using special key. The idea is as follows: whenever you find a '0', replace that row and column with 'x'
        # for all elements not equal to '0'. At the end of this operation you'll have replaced all rows and columns where 0 was present with an x.
        # the matrix now has elements, 0, and x's. In the second pass, replace all x's with 0. This will be O(m * n) time but constant space.
        m, n = len(matrix), len(matrix[0]) #row, col
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0: #replace row and column with x's
                    #row operation
                    for col, elem in enumerate(matrix[i]):
                        if elem != 0:
                            matrix[i][col] = 'x'
                    #column operation
                    for row in range(m):
                        if matrix[row][j] != 0:
                            matrix[row][j] = 'x'
        ### at this point, all rows and columns with 0's should've been replaced with x's, except for original 0's.
        #now, replace all x with 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 'x':
                    matrix[i][j] = 0