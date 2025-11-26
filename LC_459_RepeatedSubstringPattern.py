class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n=len(s)
        s1=s[1:]+s[:-1]
        #remove first and last chars
        return s in s1
        
        
