class Solution:
    def removeDuplicates(self, s: str) -> str:
        res=""
        stack=[]
        for char in s:
            if stack and char==stack[-1]:
                val=stack.pop()
            else:
                stack.append(char)
        while stack:
            res=stack.pop()+res
        return res
        
