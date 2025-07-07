class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        l=1
        maxl=1
        nums.sort()

        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]+1:
                l+=1
            elif nums[i]==nums[i-1]:
                continue
            else:
                #if not consecutive then find maxlength
                maxl=max(l,maxl)
                l=1
        
        #if last element is part of consecutive then find maxlength
        maxl=max(maxl,l)

        return maxl



            
                

        
