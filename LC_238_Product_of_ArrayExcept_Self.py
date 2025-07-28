class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[]
        l=1
        for i in range(len(nums)):
            res.append(l)
            l=l*nums[i]
        r=1
        for j in range(len(nums)-1,-1,-1):
            res[j]=res[j]*r
            r=r*nums[j]
        return res
