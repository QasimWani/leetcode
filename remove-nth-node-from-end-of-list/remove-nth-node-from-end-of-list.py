# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, k: int) -> ListNode:
        #One pass algorithm implementation
        #Time: O(n)
        #Space: O(1)
        first = second = head
        n = 0
        while(second is not None):
            second = second.next
            n += 1
            if(n > k + 1):
                first = first.next
​
        #at this point, first and second nodes are k nodes apart
        if(n == k):#remove head
            if(n == 1):
                return None
            
            first.val = first.next.val
            first.next = first.next.next
            return first
        first.next = first.next.next
        return head
