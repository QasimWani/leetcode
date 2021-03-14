# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        #basically create 2 nodes, left and right responsible for respective partitions. all nodes < x will be appended to left partition and the remaining will
        #go to right partition. this will be done in order such that at the end, left -> right will preserve the result and be the final answer.
        
        #Time: O(n)
        #Space: O(n), each left and right will have half the number of elements as head.
        
        left = right = None
        
        perm_l = left
        perm_r = right
        
        while head is not None:
            if head.val < x: #left node
                if left is None:
                    left = ListNode(head.val)
                    perm_l = left
                else:
                    left.next = ListNode(head.val)
                    left = left.next
            else:
                if right is None:
                    right = ListNode(head.val)
                    perm_r = right
                else:
                    right.next = ListNode(head.val)
                    right = right.next
                    
            head = head.next
        
        if perm_l:
            left.next = perm_r
            return perm_l
        
        #partition at smallest element: return perm_r
        return perm_r                
            
        