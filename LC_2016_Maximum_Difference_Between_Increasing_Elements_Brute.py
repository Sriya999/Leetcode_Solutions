class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        Max_diff=-1
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]<nums[j]:
                    Max_diff=max(Max_diff,nums[j]-nums[i])
        return Max_diff





         