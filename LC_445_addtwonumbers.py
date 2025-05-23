# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1,s2=[],[]#2 stacks for 2 numbers
        #numbers stored in stacks
        while l1:
            s1.append(l1.val)
            l1=l1.next
        while l2:
            s2.append(l2.val)
            l2=l2.next
        head=None
        #addition of numbers
        carry=0
        while s1 or s2 or carry:
            #extracting digits from stacks
            d1=int(s1.pop()) if s1 else 0
            d2=int(s2.pop()) if s2 else 0
            #now add
            total=d1+d2+carry
            carry=total//10
            #create node
            newnode=ListNode(total%10)
            newnode.next=head
            head=newnode
        return head

            




        
        


        
