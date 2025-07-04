# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        #binary search
        l=0
        r=n
        while l<=r:
            mid=(l+r)//2
            if isBadVersion(mid):
                r=mid-1
            else:
                l=mid+1
        return l
        
