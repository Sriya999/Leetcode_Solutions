class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s1=""
        for i in digits:
            s1=s1+str(i)
        d1=int(s1)+1
        res=list(str(d1))
        for i in range(len(res)):
            res[i]=int(res[i])
        return res
        
