# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        #we first compute the length of each linkedlist. the difference between them is how many steps we need to take for the larger one
        #such that at some point in the traversal, they must come together and that point must be the intersection. if not, then no intersection is found.
        
        #Time: O(n + m) where n and m represents the lengths of the linkedlists.
        #Space: O(1) done in-place.
        
        lenA = lenB = 0
        
        #compute the length of the first list
        curr = headA
        while curr:
            lenA += 1
            curr = curr.next
            
        #compute the length of the second list
        curr = headB
        while curr:
            lenB += 1
            curr = curr.next
        
        step = lenA - lenB
        #move list step times before moving them uniformally.
        if step > 0: #A > B, therefore move headA
            for i in range(step):
                headA = headA.next
        elif step < 0:
            for i in range(abs(step)):
                headB = headB.next

        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
            
        return None