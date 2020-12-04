# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        #Time: O(n)
        #Space: O(1)
        
        #get the size of the linked list first.
        #then iterate again and dynamically compute the value.
        size = 0
        temp = head
        while(temp is not None):
            size += 1
            temp = temp.next
        temp = head
        value = 0
size -= 1
        while(temp is not None):
            value += temp.val * 2**size
            size -= 1
            temp = temp.next
        
        return value
