class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #the idea is to perform DFS on the first character instance of word in board and return true if all characters were found in board.
        #Time: O(m x n x 3^k) where m and n are the dimensions of the board and k is the length of the word. The reason its 3 is because after
        #the first call, we can traverse to 3 different spots on the board. And at worst, keep traversing to 3 different nodes in the tree.
        #This is because we don't want to go back to the same place as we started since the positions are required to be unique.
        
        #Space: O(k) where k is the length of the word since that's the total number of recursive calls we'll be doing.
        
        m, n = len(board), len(board[0])
        if m * n < len(word):
            return False
        
        self.board = board
        
        for i in range(m):
            for j in range(n):
                if word[0] == board[i][j]:#perform search
                    if self.dfs(word, i, j):
                        return True
        return False
        
    def dfs(self,word, x, y):
        if not word: #all occurances found
            return True
        if x < 0 or x >= len(self.board) or y < 0 or y >= len(self.board[0]) or word[0] != self.board[x][y]:
            return False
        
                        
        self.board[x][y] = None
        
        #recursive calls
        if self.dfs(word[1:], x + 1, y) or self.dfs(word[1:], x - 1, y) or self.dfs(word[1:], x, y + 1) or self.dfs(word[1:], x, y - 1):
            return True
        
        self.board[x][y] = word[0]
        
        return False
