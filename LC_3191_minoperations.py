class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n=len(nums)
        minOper=0
        for i in range(n-2):
            if nums[i]==0:
                #then filp the 3 consecutive elements
                nums[i]=nums[i]^1
                nums[i+1]=nums[i+1]^1
                nums[i+2]=nums[i+2]^1
                minOper+=1
        if nums[-1]==0 or nums[-2]==0:
            return -1
        return minOper


        
        
