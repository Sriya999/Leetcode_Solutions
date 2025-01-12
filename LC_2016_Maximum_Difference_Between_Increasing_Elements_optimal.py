class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        diff=-1
        low=nums[0]
        for i in range(1,len(nums)):
            if low<nums[i]:
                temp=nums[i]-low
                diff=max(diff,temp)
            low=min(low,nums[i])
        return diff


            
      