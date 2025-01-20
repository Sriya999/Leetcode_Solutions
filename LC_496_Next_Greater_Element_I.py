class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        def findnextgreat(j,k,nums2):
                        
            for i in range(j,len(nums2)):
                if nums2[i]>nums2[j]:
                    return nums2[i]
            return -1 	   
        for i in range(0,len(nums1)):
            for j in range(0,len(nums2)):
                if nums1[i]==nums2[j]:
                    #print(nums1[i],"----index---at ",i,j)
                    res=findnextgreat(j,len(nums2),nums2)
                    ans.append(res)
        return ans
            
                    