# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #keep track of prev node curr node next node using 3 pointers
        prev=None
        temp=head
        while temp:
            front=temp.next#next node
            temp.next=prev#link to prev node
            prev=temp
            temp=front
        return prev

        
        
