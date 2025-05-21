class Solution:
    def longestPalindrome(self, s: str) -> str:
        def ispalindrome(s):
            return s==s[::-1]
               
        
        if len(s)==1:
            return s
        elif len(s)==0:
            return ""
        
        res=s[0]
        maxLen=1
        for i in range(0,len(s)):
            for j in range(i+1,len(s)):
                substr=s[i:j+1]
                substrlen=len(substr)
                if ispalindrome(substr) and maxLen<substrlen:
                    res=substr
                    maxLen=substrlen
        return res

   
