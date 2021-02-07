# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        #the idea is to use the Sentinel head + Predecessor approach.
        #We have a default node prepended to current head node in the case all elements equal head
        #so we basically do what we did before in finding all unique elements LC problem.
        #but this time, instead of simply appending (meaning we'd have added current unique node as well),
        #we append the node.next of it such that no node that has occured multiple times is added to list.
        
        #Time : O(n)
        #Space : O(1)
        
        sentinel = ListNode(0, head) #prepend the head to prevent from duplicates
        
        pred = sentinel #predecessor node (similar to `node` in remove-duplicates-from-sorted-list-i)
        
        while head and head.next:
            
            if head.next.val == head.val: #remove all nodes within this range include current node, head
                while head.next and head.next.val == head.val: #keeps removing all nodes.
                    head = head.next
                pred.next = head.next #now, remove head node as well such that head.prev = head.next; skips all duplicates
                
            else:
                pred = pred.next #move precessor
            
            head = head.next #perform regular iteration
        
        return sentinel.next