#User function Template for python3
from collections import deque 
class Solution:
    def firstNegInt(self, arr, k):
        res=[]
        dq=deque()
        l=0
        for r in range(len(arr)):
            #keep track of window
            if dq and dq[0]<r-k+1:
                dq.popleft()
            #add neg to deque
            if arr[r]<0:
                dq.append(r)
            #add result
            if r>=k-1:
                if dq:
                    res.append(arr[dq[0]])
                else:
                    res.append(0)
        return res
                
            
        
        
            
            
            
        
    
          
