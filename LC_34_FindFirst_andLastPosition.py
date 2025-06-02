class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        idx1=-1
        idx2=-1

        for i in range(len(nums)):
            if nums[i]==target:
                idx1=i
                break
                
        for i in range(len(nums)-1,-1,-1):
            if nums[i]==target:
                idx2=i
                break
        return [idx1,idx2]
