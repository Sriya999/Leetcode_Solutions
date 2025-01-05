class Solution:
    def myAtoi(self, s: str) -> int:
       
        s=s.lstrip()

        if len(s)==0:
            return 0
        
        sign=1
        #pointer i
        i=0
        if s[i]=='-':
            sign=-1
            i=1
        elif s[i]=='+':
            i=1
        ans=0
        #INT MAX INT MIN VALUES
        maxi=2**31-1
        mini=-2**31
        while(i<len(s)):
            if s[i].isdigit():
                ans=ans*10+int(s[i])
                if sign==-1 and sign*ans<mini:
                    return mini
                elif sign==1 and sign*ans>maxi:
                    return maxi
            else:
                break
            i=i+1
        
        
        return ans*sign
            
            


        