# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        #This problem was trivial to solve after solving the "largest diameter of a Binary Tree" problem. Simple DFS recursive solution with some
        #max criterias solves this optimally.
        #Time: O(n)
        #Space: O(log(n)) = O(h)
        
        self.max_sum = float('-inf')
        self.dfs(root)
        
        return self.max_sum
    
    def dfs(self, node):
        if not node:
            return 0
        
        left_sum = self.dfs(node.left)
        right_sum = self.dfs(node.right)
        
        #breakdown of the 4 cases. 
        #case I   -  max sum is just the current node
        #case II  -  max sum is the left path plus the current node
        #case III -  max sum is the right path plus the current node
        #case IV  -  max sum is the combination of left and right paths plus the current node
        self.max_sum = max(self.max_sum, node.val, node.val + max(left_sum, right_sum, left_sum + right_sum))
        
        return max(node.val, max(left_sum, right_sum) + node.val)