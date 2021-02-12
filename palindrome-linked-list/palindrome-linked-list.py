# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        #the idea is to reverse the second half and check to see if it equals the second half.
        slow = fast = head
        #find the middle node
        while fast and fast.next is not None:
            fast = fast.next.next
            slow = slow.next #1/2 speed of fast
        
        #reverse second half
        prev = None
        while slow:
            temp = slow
            slow = slow.next
            temp.next = prev
            prev = temp
        
        #now, simply compare the first and second halfs
        while prev is not None:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        return True