# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        #The idea is to get the length of each list and traverse the smaller list once n - k nodes of the larger node have been traversed. Here
        #n is the length of the larger list and k is the length of the smaller list. While traversing, simply store the sum in an array, ignoring
        #any carry calculations. After this, we traverse the result from the end to get the refined output and store it accordingly. After this,
        #just reconstruct the List.
        #Time: O(N1 + N2) where N1 and N2 are the sizes of the 2 lists
        #Space: O(max(N1, N2))
        
        num1, num2 = self.getNodes(l1), self.getNodes(l2)
        
        if num1 < num2:
            return self.addTwoNumbers(l2, l1)
        
        head1, head2 = l1, l2
        i = 0
        sum = []
        
        while head1:
            if i >= num1 - num2:
                sum.append(head1.val + head2.val)
                head2 = head2.next
            else:
                sum.append(head1.val)
                
            head1 = head1.next
            i += 1
        
        carry = 0
        for i in range(len(sum) - 1, -1, -1):
            x = sum[i]
            sum[i] = (x + carry) % 10
            carry = (x + carry) // 10
            
        #add carry bit for the first integer
        start = 1
        fx = sum[0]
        if carry:
            start = 0
            fx = 1
            
        lsum = ListNode(fx)
        head = lsum
        
        for i in range(start, len(sum)):
            head.next = ListNode(sum[i])
            head = head.next
        return lsum
            
        
        
    def getNodes(self, root):
        """Returns the number of nodes in a linked list with root"""
        head = root
        num = 0
        while head:
            head = head.next
            num += 1
        return num
        