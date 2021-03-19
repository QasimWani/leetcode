# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        #use the trick of using a for loop within a while loop for traversing a tree using BFS.
        
        #Time: O(N)
        #Space: O(N)
        
        levels = []
        
        if not root:
            return levels
        
        queue = [root]
        
        while queue:
            levels.append([])
            
            for i in range(len(queue)):
                node = queue.pop(0)
                
                levels[-1].append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            
        return levels