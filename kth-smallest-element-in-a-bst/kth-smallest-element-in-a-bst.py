# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        #using inorder traversal we can find the kth smallest node in the BST.
        
        #Time: O(n) where n is the number of nodes
        #Space: O(n)
        
        array = []
        self.traversal(root, array)
        return array[k - 1]
            
    def traversal(self, root, arr):
        if not root:
            return
        self.traversal(root.left, arr)
        arr += [root.val]
        self.traversal(root.right, arr)