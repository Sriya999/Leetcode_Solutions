class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res=set()
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            visited=set()
            for j in range(i+1,len(nums)):
                third=-(nums[i]+nums[j])
                if third in visited:
                    res.add(tuple(sorted([nums[i],nums[j],third])))
                else:
                    visited.add(nums[j])
        return [list(t) for t in res]






















        


        
