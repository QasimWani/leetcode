# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # if list is sorted, node.val <= node.next.val
        # therefore, we keep deleting nodes while node.val == node.next.val
        # such that node.val is strictly lesser than node.next.val
        
        #Space: O(1)
        #Time: O(n)
        
        node = head
        while node is not None and node.next is not None:
            if node.next.val == node.val:
                node.next = node.next.next
            else:
                node = node.next
        return head