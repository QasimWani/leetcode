"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Node':
        #basically 2 cases:
        # 1) Leaf node - find the parent node greater than current node. basically find the first parent node greater than itself.
        # 2) Parent node - find the smallest node greater than itself, i.e. left most node on the right side of the tree.
        
        # Overall Time: O(log(n)) where n is the number of nodes. In other words, O(h) where h is the height of the tree.
        # Overall Space: O(1)
        
        if self.has_right_child(node): #case (2)
            node = node.right
            while node.left:
                node = node.left
            return node
        else:#leaf node.
            parent_node = node.parent
            while parent_node:
                if parent_node.val > node.val:
                    return parent_node
                parent_node = parent_node.parent
            return None
            
    def has_right_child(self, node):
        return node.right
        