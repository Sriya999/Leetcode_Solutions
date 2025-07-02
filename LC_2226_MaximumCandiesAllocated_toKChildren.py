class Solution:
    def isPossible(self,candies,k,c):
        for i in range(len(candies)):
            k=k-candies[i]//c
            if k<=0:
                return True
        return False
    def maximumCandies(self, candies: List[int], k: int) -> int:
        l=1
        r=max(candies)
        while l<=r:
            mid=(l+r)//2
            if self.isPossible(candies,k,mid):
                l=mid+1
            else:
                r=mid-1
        return r
        
        
