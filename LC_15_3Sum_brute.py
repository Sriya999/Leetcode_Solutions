class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=set()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if nums[i]+nums[j]+nums[k]==0:
                        res.add(tuple(sorted([nums[i],nums[j],nums[k]])))
        print(res)
        return [list(t) for t in res]


        


        
