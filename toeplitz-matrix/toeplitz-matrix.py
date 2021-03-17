class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        #basically check if the adjacent diagonals are all equivalent to one another. if not, return false
        #Time: O(n x m)
        #Space: O(1)
        
        m,n = len(matrix), len(matrix[0])
        for i in range(m - 1):
            for j in range(n - 1):
                if matrix[i][j] != matrix[i + 1][j + 1]:
                    return False
        return True
        