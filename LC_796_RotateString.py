class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False
        n=len(s)
        k=1
        for i in range(len(s)):
            s=s[k:]+s[:k]
            if s==goal:
                return True
        return False
        
