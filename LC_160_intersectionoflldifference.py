# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        def collisionpoint(t1,t2,d):
            while d:
                d-=1#eliminating distance and pointing at corresponding level
                t2=t2.next
            while t1!=t2:
                t1=t1.next
                t2=t2.next
            return t1
        
        #find length of lists
        n1=0
        n2=0
        temp1=headA
        while temp1:
            n1+=1
            temp1=temp1.next
        temp2=headB
        while temp2:
            n2+=1
            temp2=temp2.next
        

        if n1<n2:
            return collisionpoint(headA,headB,n2-n1)
        else:
            return collisionpoint(headB,headA,n1-n2)
        
        
        

        
