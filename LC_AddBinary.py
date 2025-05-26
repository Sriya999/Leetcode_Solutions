class Solution:
    def addBinary(self, a: str, b: str) -> str:
        #binary to decimal
        a=int(a,2)
        b=int(b,2)
        #adding decimal numbers
        res=a+b
        #result converted to binary
        return bin(res)[2:]
