class Solution:
    def is_basek_palindrome(self,num,k):
        #convert to base k
        res=""
        while num>0:
            d=num%k
            res=str(d)+res
            num=num//k
        return res==res[::-1]
    def kMirror(self, k: int, n: int) -> int:
        sum1=0
        l=1
        while n>0:
            half_l=(l+1)//2
            start=10**(half_l-1)
            end=10**half_l
            for half in range(start,end):
                half=str(half)
                if l%2==1:#odd palindrome
                    pal=half+half[-2::-1]
                else:#even palindrome
                    pal=half+half[::-1]
                pal=int(pal)
                #base k palindrome
                if self.is_basek_palindrome(pal,k):
                    sum1=sum1+pal
                    n=n-1
                    if n==0:
                        break
            l+=1
        return sum1
                
