class Solution:
    def isHappy(self, n: int) -> bool:
        visit=set()

        while n!=1 and n not in visit:
            visit.add(n)
            output=0
            while n>0:
                digit=n%10
                output=output+digit*digit
                n=n//10
            n=output

        if n==1:
            return True
        else:
            return False

        