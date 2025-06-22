# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,node):
        """reverses the list """
        prev=None
        temp=node
        while temp:
            front=temp.next
            temp.next=prev
            prev=temp
            temp=front
        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
            """
        #find first middle
        slow=head
        fast=head
        #odd,even
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        #cutting first half
        second_half=self.reverse(slow.next)
        slow.next=None

        #merge them
        first=head
        second=second_half
        while first and second:
            firstnext=first.next#saving the next nodes
            secondnext=second.next
            first.next=second
            second.next=firstnext
            first=firstnext
            second=secondnext
        return head
        

        


                

        
