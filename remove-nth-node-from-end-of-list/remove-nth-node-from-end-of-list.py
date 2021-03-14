# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, k: int) -> ListNode:
        #simple one-pass algorithm. have 2 pointers. the first pointer iterates continously.
        #the second pointer starts iterating once the first pointer crosses k nodes. the second pointer
        #stops when the first pointer hits the end, thereby making the second pointer stop at N - k - 1 node.
        #so, the second pointer removes the next node.
        
        #Time: O(n)
        #Space: O(1)
        
        current = runner = head
        i = 0
        while current is not None:
            current = current.next
            i += 1
            if i > k + 1: #start moving the second pointer
                runner = runner.next
        
        #remove runner.next
        if i == k:#remove head
            return None if i == 1 else runner.next
        
        runner.next = runner.next.next if runner.next.next is not None else None
        return head
    
    
            