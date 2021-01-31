# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        dl1, dl2 = '', '' #represents the digits of l1 and l2 lists, respectively
        
        #iterate through each list and get the digits
        while(l1 is not None):
            dl1 += str(l1.val)
            l1 = l1.next
            
        while(l2 is not None):
            dl2 += str(l2.val)
            l2 = l2.next
        
        sum = str(int(dl1[::-1]) + int(dl2[::-1]))

        head = ListNode()
        temp = head
        for i, char in enumerate(sum[::-1]):
            temp.val = char
            temp.next = ListNode() if i < len(sum) - 1 else None
            temp = temp.next
            
        return head