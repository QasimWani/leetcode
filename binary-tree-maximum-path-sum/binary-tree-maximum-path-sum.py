# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max_sum = float('-inf')
        self.dfs(root)
        return self.max_sum
    
    def dfs(self, node):
        if not node:
            return 0
        left_sum = self.dfs(node.left)
        right_sum = self.dfs(node.right)
        
        self.max_sum = max(self.max_sum, left_sum + node.val, right_sum + node.val, left_sum + right_sum + node.val, node.val)
        
        return max(node.val, max(left_sum, right_sum) + node.val)