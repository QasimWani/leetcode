# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        #BFS with levels using for loop trick.
        
        #Time: O(N), where N is the number of nodes in the tree
        #Space: O(H), where H is the height of the tree
        
        levels = []
        if not root:
            return levels
        
        queue = [root]
        levels.append(root.val)
        
        while queue:
            val = None
            for i in range(len(queue)):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                    val = node.left.val
                if node.right:
                    queue.append(node.right)
                    val = node.right.val
            if val:
                levels.append(val)
        return levels