# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #the idea is to generate a path from root to ancestor node i.e. p and q as an array.
        #from there, we are essentially traversing the arrays and seeing which of the latest nodes is the same for path p and path q.
        
        #Time: O(log(n)) = O(d) where d is the depth of the tree.
        #Space: O(log(n)) = O(d) because we're storing the path as auxillary memory.
        
        path_p, path_q = [root], [root]
        
        temp = root
        #generate path for p node
        while temp.val != p.val:
            if temp.val > p.val:#left
                temp = temp.left
            else:
                temp = temp.right
            path_p.append(temp)
            
        
        temp = root
        #generate path for p node
        while temp.val != q.val:
            if temp.val > q.val:#left
                temp = temp.left
            else:
                temp = temp.right
            path_q.append(temp)     
        
        
        #find youngest ancestor.
        youngest = None
        for a, b in zip(path_p, path_q):
            if a.val == b.val:
                youngest = a
        return youngest
        