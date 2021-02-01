# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        #value = max(children, parent + next children), i.e. max(children, parent + parent->children->children)
        
        def helper(node):
            if(node is None):
                return (0,0)#left and right child

            left = helper(node.left)
            right = helper(node.right)

            chr = node.val + left[1] + right[1]

            return [chr, max(left) + max(right)]
        
        return max(helper(root))