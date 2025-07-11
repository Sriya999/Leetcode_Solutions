# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        fast=dummy
        slow=dummy

        #fast pointer advance n steps ahead
        for i in range(n+1):
            fast=fast.next
        
        while fast:
            slow=slow.next
            fast=fast.next
        #removing nth node
        slow.next=slow.next.next
        return dummy.next





        
