class Solution:
    def isposs(self,piles,k,h):
        for pile in piles:
            h=h-math.ceil(pile/k)
            if h<0:
                return False
        return True
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=math.pow(10,9)
        while l<=r:
            mid=(l+r)//2
            if self.isposs(piles,mid,h):
                 r=mid-1
            else:
                l=mid+1
        return int(l)
