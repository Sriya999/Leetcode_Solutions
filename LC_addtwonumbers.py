# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry,total=0,0
        dummy=ListNode(0)
        curr=dummy
        while l1 or l2 or carry:
            total=carry
            if l1:
                total=total+l1.val
                l1=l1.next
            if l2:
                total=total+l2.val
                l2=l2.next
            carry=total//10
            #creates node
            curr.next=ListNode(total%10)
            curr=curr.next

            
        return dummy.next

            




            




        
        
        
