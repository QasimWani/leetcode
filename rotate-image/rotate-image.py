class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #the idea is to have a set of pointers representing the dimensions of the matrix
        #that'd move inwards after each set of rotation.
        #so the core logic is take the elements from top, right, down, and left.
        #and make top = right, right = down, down = left, and left = top.
        #once that's done, move all pointers down by one. repeat the process.
        
        #Time: O(n^2), where n is the number or rows/columns in the matrix
        #Space: O(1)
        
        n = len(matrix)
        
        for first in range(n//2):
            last = n - 1 - first
            for i in range(first, last):
                offset = i - first
                #save the top element
                top = matrix[first][i]
                #move left->top
                matrix[first][i] = matrix[last - offset][first]
                #move bottom->left
                matrix[last - offset][first] = matrix[last][last - offset]
                #move right->bottom
                matrix[last][last - offset] = matrix[i][last]
                #move top->right
                matrix[i][last] = top