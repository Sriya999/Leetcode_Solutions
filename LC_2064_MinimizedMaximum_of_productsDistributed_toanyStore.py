class Solution:
    def isPossible(self,n,quantities,d):
        for i in range(len(quantities)):
            val=quantities[i]/d
            n=n-int(math.ceil(val))
            if n<0:
                return False
        return True

    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        l=1
        r=10**5
        while l<=r:
            mid=l+(r-l)//2
            if self.isPossible(n,quantities,mid):
                r=mid-1
            else:
                l=mid+1
        return l
        
