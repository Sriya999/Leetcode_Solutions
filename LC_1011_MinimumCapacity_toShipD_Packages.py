class Solution:
    def isPossible(self,weights,c,k):
        total=0
        for i in range(len(weights)):
            if weights[i]>c:
                return False
            if total+weights[i]>c:
                k=k-1
                total=0
            total=total+weights[i]
            if k<=0:
                return False
        return True

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l=max(weights)
        r=sum(weights)
        while l<=r:
            mid=(l+r)//2
            if self.isPossible(weights,mid,days):
                r=mid-1
            else:
                l=mid+1
        return l

        
