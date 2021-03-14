# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        #super simple. have 2 pointers, one slow and one fast. the fast pointer moves 2x the speed of slow pointer which moves one step at a time.
        #when the fast pointer reaches the end of the node, the slow pointer will be at the middle node.
        
        #Time: O(n)
        #Space: O(1)
        
        slow = fast = head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow
        