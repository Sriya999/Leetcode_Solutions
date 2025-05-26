class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        temp=0
        ans= float('inf')
        l=0
        for r in range(0,len(nums)):
            temp=temp+nums[r]
            while temp>=target:
                ans=min(ans,r-l+1)
                temp=temp-nums[l]
                l+=1
        if ans==float('inf'):
            return 0
        else:
            return ans
