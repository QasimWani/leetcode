# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, tree: TreeNode,  min_value = float('-inf'), max_value = float('inf')) -> bool:
        # Write your code here.
        if(tree is None):
            return True
        if(tree.val <= min_value or tree.val >= max_value):
            return False
        return self.isValidBST(tree.left, min_value, tree.val) and self.isValidBST(tree.right, tree.val, max_value)
