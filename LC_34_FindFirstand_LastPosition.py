class Solution:
    def leftmost(self,nums,target):
        l=0
        r=len(nums)-1
        while l<=r:
            mid=l+(r-l)//2
            if nums[mid]==target:
                r=mid-1
            elif nums[mid]>target:
                r=mid-1
            else:
                l=mid+1
        if l>=len(nums):
            return -1
        if nums[l]!=target:
            return -1
        return l
    def rightmost(self,nums,target):
        l=0
        r=len(nums)-1
        while l<=r:
            mid=l+(r-l)//2
            if nums[mid]==target:
                l=mid+1
            elif nums[mid]<target:
                l=mid+1
            else:
                r=mid-1
        if r<0:
            return -1
        if nums[r]!=target:
            return -1
        return r


    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.leftmost(nums,target),self.rightmost(nums,target)]
        
