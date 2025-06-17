# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #find middle
        slow=head
        fast=head
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        #reverse the second half ll
        def reverse(node):
            temp=node
            prev=None
            while temp:
                front=temp.next
                temp.next=prev
                prev=temp
                temp=front
            return prev
        secondhalf=reverse(slow.next)
        #compare values of both halves
        first=head
        second=secondhalf
        while second:
            if first.val!=second.val:
                reverse(secondhalf)
                return False
            first=first.next
            second=second.next
        reverse(secondhalf)
        return True

