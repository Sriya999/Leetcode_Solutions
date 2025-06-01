class Solution:
    def atmostsubarr(self,nums,k):
        l,temp,ans=0,0,0
        dict1=dict()
        for r in range(0,len(nums)):
            dict1[nums[r]]=dict1.get(nums[r],0)+1
            while len(dict1)>k:
                dict1[nums[l]]=dict1.get(nums[l])-1
                if dict1[nums[l]]==0:
                    del dict1[nums[l]]
                l+=1
            ans=ans+r-l+1
        return ans

    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.atmostsubarr(nums,k)-self.atmostsubarr(nums,k-1)
