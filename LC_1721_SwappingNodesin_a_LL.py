# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr=head
        #setting left pointer to left kth node
        for i in range(1,k):
            curr=curr.next
        left=curr
        right=head
        #setting right node k th node from end
        while curr.next:
            curr=curr.next
            right=right.next
        left.val,right.val=right.val,left.val
        return head

        
