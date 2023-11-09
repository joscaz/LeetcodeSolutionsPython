class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        symbols = {'[':']', '{':'}', '(':')'}

        for bracket in s:
            if bracket in symbols:
                stack.append(bracket)
            
            elif len(stack) == 0 or bracket != symbols[stack.pop()]:
                return False
 
        return len(stack) == 0