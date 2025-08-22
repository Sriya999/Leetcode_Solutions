class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum=0
        maxSum=float('-inf')
        for i in range(len(nums)):
            currSum=currSum+nums[i]
            maxSum=max(currSum,maxSum)
            #if negative sum then ignore as it cannot make maximum for nxt subarrays
            if currSum<0:
                currSum=0
        return maxSum
        
