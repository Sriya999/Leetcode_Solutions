# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr=head
        #count nodes
        length=0
        temp=head
        while temp:
            length+=1
            temp=temp.next
        #finding left node
        for i in range(1,k):
            curr=curr.next
        left=curr
        #finding right node
        ryt=head
        for i in range(1,length-k+1):
            ryt=ryt.next
        #swap values left and right nodes
        left.val,ryt.val=ryt.val,left.val
        return head

        
