class Solution:
    def isPos(self,nums,div,threshold):
            sum1=0
            for num in nums:
                u=math.ceil(num/div)
                threshold=threshold-u
                if threshold<0:
                    return False
            return True
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l=1
        r=1000000
        while l<=r:
            mid=(l+r)//2
            if self.isPos(nums,mid,threshold):
                r=mid-1
            else:
                l=mid+1
        return l
