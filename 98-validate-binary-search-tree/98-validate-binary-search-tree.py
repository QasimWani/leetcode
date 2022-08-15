# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode], upper_bound=float('inf'), lower_bound=float('-inf')) -> bool:
        # essentially, the left node should be lesser than parent node and the right node should be greater than parent node.
        if not root:
            return True
        if root.val >= upper_bound or root.val <= lower_bound:
            return False
        
        return self.isValidBST(root.left, root.val, lower_bound) and self.isValidBST(root.right, upper_bound, root.val)
            
            