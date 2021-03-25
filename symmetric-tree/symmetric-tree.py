# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        #Use BFS and gather all nodes at level l and see if all the values at that node are symetric by using 2 pointers. Using a stack.
        #Time = O(N)
        #Space = O(N)
        
        queue = [root]
        
        while queue:
            left, right = 0, len(queue) - 1
            while left <= right:
                if queue[left] and queue[right] and queue[left].val != queue[right].val:
                    return False
                if queue[left] and not queue[right] or not queue[left] and queue[right]:
                    return False
                left += 1
                right -= 1
                
            for i in range(len(queue)):
                node = queue.pop(0)
                if node:
                    queue.append(node.left)
                    queue.append(node.right)
                    
        return True