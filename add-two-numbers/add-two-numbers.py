# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        #Time: O(max(n,m)) where n and m are the lengths of l1 and l2, respectively.
        #Space: O(max(n, m))
        
        list = ListNode()
        head = list
        
        while l1 or l2:
            a = b = 0
            if l1:
                a = l1.val
                l1 = l1.next
            if l2:
                b = l2.val
                l2 = l2.next
            
            sum = list.val + a + b
            carry = sum // 10
            
            list.val = sum % 10

            list.next = ListNode(carry) if carry or l1 or l2 else None
            list = list.next
            
        return head