# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        #2 pointer approach, one a slow pointer and a fast pointer that moves twice as fast
        #as the slow pointer. if the slow pointer is ever equal to fast pointer, cycle exists
        #Once we know we found a cycle, we iterate slow and fast again, but this time with
        #same speed. however, we start slow with head. The node that they reach this time will
        #be the node that resulted in the cycle.
        
        #Time: O(n)
        #Space: O(1)
        
        if(head is None):
            return None
        slow = fast = head
        
        while fast is not None:
            if fast.next is None:
                return None
            
            fast = fast.next.next
            slow = slow.next
            
            if(slow == fast):
                slow = head
                while fast is not slow:
                    slow = slow.next
                    fast = fast.next
                return fast
            
        return None