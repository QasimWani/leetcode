# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        #The idea is to DFS the tree and get the length of left and right tree from current node and see if that's greater than the diameter.
        #If so, that's the new diameter. 
        
        #Time = Space: O(N)
        
        self.diameter = 0
        self.dfs(root)
        return self.diameter
    
    def dfs(self, node):
        if not node:
            return 0
        
        left, right = self.dfs(node.left), self.dfs(node.right)
        
        self.diameter = max(self.diameter, left + right)
        return max(left, right) + 1