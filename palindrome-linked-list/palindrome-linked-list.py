# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        #Time: O(N)
        #Space: O(1) done in-place
        
        #the idea is to get to the half of the list, reverse the second half, and compare if it equals the first half
        slow = fast = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        #at this point, the slow pointer is at the half of the list. We now reverse the second half.
        prev = None
        while slow:
            temp = slow
            slow = slow.next
            temp.next = prev
            prev = temp
        
        #at this point, we've now reversed the second half of the list. we now check to see if the first half matches prev.
        while prev:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
        return True