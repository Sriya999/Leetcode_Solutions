class Solution:
    def averageValue(self, nums: List[int]) -> int:
        ans=0
        totall=0
        s=0
        for i in range(len(nums)):
            if nums[i]%3==0 and nums[i]%2==0:
                totall+=nums[i]
                s+=1
        if s==0:
            return 0
        else:
            ans=totall//s
            return ans