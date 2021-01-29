# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        #instead of deleting `node`, delete node.next but get node.next value and store it in node.val
        #this is because we don't have access to head ptr.
        
        node.val = node.next.val
        node.next = node.next.next