class Solution:
    def isPossible(self,nums,maxo,k):
        for i in range(len(nums)):
            maxo=maxo-(math.ceil(nums[i]/k)-1)
            if maxo<0:
                return False
        return True

    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        r=max(nums)
        l=1
        while l<=r:
            mid=l+(r-l)//2
            if self.isPossible(nums,maxOperations,mid):
                r=mid-1
            else:
                l=mid+1
        return l
            
        
