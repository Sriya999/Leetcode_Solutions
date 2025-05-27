class Solution:
    def countBits(self, n: int) -> List[int]:
        a=[0]*(n+1)
        for i in range(0,len(a)):
            a[i]=a[i>>1]+(i&1)
        return a
