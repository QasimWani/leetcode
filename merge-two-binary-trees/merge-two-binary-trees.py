# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        #the idea is quite simple, perform a recursive BFS on one of the trees and add the values on each call.
        #Time: O(n), n = min(number of nodes in t1, number of nodes in t2)
        #Space: O(n)
        
        if(t1 is None):
            return t2
        if(t2 is None):
            return t1
        
        t1.val += t2.val

        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        
        return t1

        
        
        
            
            
        
        
            
        