# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
​
class Codec:
​
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        #perform BST and append nodes to a string. "N" represents none val.
        #Time: O(n)
        #Space: O(2^h), where h represents the maximum depth of the tree.
        queue = [root]
        
        if(not root):
            return ' null'
        
        return " " + str(root.val) + self.serialize(root.left) + self.serialize(root.right)
​
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        ### deconstruct the string.
        code = data.split(" ")[1:]
        print(code)
        return self.construction(code)
    
    def construction(self, arr):
        """Constructs a Binary tree"""
        if(arr[0] == "null"):
            arr.pop(0)
            return None
        root = TreeNode(arr[0])
        arr.pop(0)
        root.left = self.construction(arr)
        root.right = self.construction(arr)
        
        return root
        
​
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
