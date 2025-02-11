class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
    
        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            elif char == ')' or char == '}' or char == ']':
                if not stack:
                    return False
                top_element = stack.pop()
                if char == ')' and top_element != '(':
                    return False
                elif char == '}' and top_element != '{':
                    return False
                elif char == ']' and top_element != '[':
                    return False

        return len(stack)==0