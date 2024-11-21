class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        symbols = {'{':'}', '(':')', '[':']'}

        for c in s:
            if c in symbols:
                stack.append(c)
            elif stack and symbols[stack.pop()] == c:
                continue
            else:
                return False
            
        return True if not stack else False
        
        '''
        ((}'''