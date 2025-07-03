class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        res=0
        for i in operations:
            if i=="+":
                if stack:
                    a=stack[-1]
                    b=stack[-2]
                    stack.append(a+b)
            elif i=="D":
                stack.append(stack[-1]*2)
            elif i=="C":
                stack.pop()
            else:
                stack.append(int(i))
        while stack:
            res=res+stack.pop()
        return res
        

        
