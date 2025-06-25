class Solution:
    def isPossible(self,bloom,k,m,bloomDay):
        took=0
        for i in range(len(bloomDay)):
            if bloom>=bloomDay[i]:
                took+=1
            else:
                #if not adjacent--newly start day
                took=0
            if took==k:
                m=m-1
                took=0#start new bouquet
        return m<=0

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay)<(m*k):#if flowers are lacking then we cant make enough bouquets
            return -1
        l=1
        r=max(bloomDay)
        while l<=r:
            mid=l+(r-l)//2
            if self.isPossible(mid,k,m,bloomDay):
                r=mid-1
            else:
                l=mid+1
        return l
        
        
