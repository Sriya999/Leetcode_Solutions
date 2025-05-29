class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        return self.atmostgoal(nums,goal)-self.atmostgoal(nums,goal-1)
 
    def atmostgoal(self,nums,goal):
        if goal<0:
            return 0
        temp,ans=0,0
        l=0 #left pointer
        for r in range(len(nums)):
            temp=temp+nums[r]
            while temp>goal:
                temp=temp-nums[l]
                l+=1
            ans=ans+r-l+1
        return ans
        
