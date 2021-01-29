# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        #perform DFS and have running counter of max height
        #Time = O(n)
        #Space = O(logn)
        
        if(root is None):
            return 0

        return max(self.maxDepth(root.left) + 1, self.maxDepth(root.right) + 1)