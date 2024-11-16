class Solution:
    def isValid(self, s: str) -> bool:
        par = {'{':'}', '(':')', '[':']'}
        stack = []

        for c in s:
            if c in par:
                stack.append(c)
            elif stack and par[stack.pop()] == c:
                continue
            else:
                return False
        
        return True if not stack else False