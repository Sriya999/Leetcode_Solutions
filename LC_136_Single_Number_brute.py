class Solution:
    def singleNumber(self, nums: List[int]) -> int:
       
        for i in range(0,len(nums)):
           if nums.count(nums[i])==1:
               return nums[i]
          
        return -1
        