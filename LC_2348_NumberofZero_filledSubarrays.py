class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans=0
        c=0
        for i in range(len(nums)):
            if nums[i]==0:
                c+=1
                ans=ans+c
            else:
                c=0
        return ans
