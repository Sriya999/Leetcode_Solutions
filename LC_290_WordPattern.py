class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mapp=dict()
        sl=list(s.split())
        if len(pattern)!=len(sl):
            return False
        for i in range(len(pattern)):
            if pattern[i] in mapp:
                if mapp[pattern[i]]!=sl[i]:
                    return False
            else:
                mapp[pattern[i]]=sl[i]
        
        #reverse mapping
        rev=dict()
        for i in range(len(sl)):
            if sl[i] in rev:
                if rev[sl[i]]!=pattern[i]:
                    return False
            else:
                rev[sl[i]]=pattern[i]
        return True
            

