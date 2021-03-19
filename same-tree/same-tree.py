# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        #basically do a DFS on p and q with reference to one of the trees, say p and compare the values.
        
        #Time: O(n)
        #Space: O(n)
        
        if not (p or q):
            return True
        if not (p and q):
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
        