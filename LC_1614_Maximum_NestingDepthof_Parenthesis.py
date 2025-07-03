class Solution:
    def maxDepth(self, s: str) -> int:
        depth=0
        
        stack=[]
        for i in s:
            if  i=="(":
                stack.append("(")
            elif i==")":
                depth=max(len(stack),depth)
                while stack and stack[-1]!="(":
                    stack.pop()
                stack.pop() 
        return depth
   
            
