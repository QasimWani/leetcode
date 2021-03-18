# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #Basically finding the lowest common ancestor of BST but now with a binary tree, we just use generalized DFS to find the path for each node, p and q.
        
        #Time: O(N)
        #Space: O(N)
        
        path_p = self.generate_path(root, p, [root])
        path_q = self.generate_path(root, q, [root])
        
        youngest = None
        for p, q in zip(path_p, path_q):
            if p.val == q.val:
                youngest = p
        return youngest
        
    def generate_path(self, root, node, path):
        """Using DFS to find the node"""
        if root is None:
            return
        if root.val == node.val:
            return path
        
        return self.generate_path(root.left, node, path + [root.left]) or self.generate_path(root.right, node, path + [root.right])