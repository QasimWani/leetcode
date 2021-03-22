# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        #perform BFS and check to see if current subtree equals t.
        #Time: O(m x n) where m and n are the number of nodes in s and t.
        #Space: O(m x n) 
        
        queue = [s]
        while queue:
            node = queue.pop(0)
            if node.val == t.val:
                if self.isSameTree(node, t): return True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return False
    
    def isSameTree(self, p, q):
        if not (p or q):
            return True
        if not (p and q):
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)