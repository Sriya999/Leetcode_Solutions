class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        sub=[]
        def getsubsets(i,res):
            if i>=n:
                sub.append(res[:])
                return
            res.append(nums[i])
            #include
            getsubsets(i+1,res)
            #backtrack
            res.pop()
            #exclude
            getsubsets(i+1,res)
        getsubsets(0,[])
        return sub
    

        
