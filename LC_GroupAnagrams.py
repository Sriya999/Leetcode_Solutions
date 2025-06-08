class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a=dict()
        for i in range(len(strs)):
            key=''.join(sorted(strs[i]))
            if key in a:
                a[key].append(strs[i])
            else:
                a[key]=[]
                a[key].append(strs[i])
        res=[]
        for key,val in a.items():
            res.append(val)
        return res
            
