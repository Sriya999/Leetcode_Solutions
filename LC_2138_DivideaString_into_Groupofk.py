class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        res=[]
        for r in range(0,len(s),k):
            substr=s[r:r+k]
            res.append(substr)
        if len(res[-1])<k:
            for i in range(k-len(res[-1])):
                res[-1]=res[-1]+fill
        return res

        
