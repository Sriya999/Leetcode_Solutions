class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l=i+1
            r=len(nums)-1
            while l<r:
                total=nums[i]+nums[l]+nums[r]
                if total>0:
                    r-=1
                elif total<0:
                    l+=1
                else:
                    #TOTAL=0
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    #skip duplicate triplet
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
                    while nums[r]==nums[r-1] and l<r:
                        r-=1
        return res

                    



















        


        
