class Solution:
    def isValid(self, s: str) -> bool:
        symb = {'(':')', '[':']', '{':'}'}
        stack = []


        for c in s:
            if c in symb:
                stack.append(c)
            elif stack and c == symb[stack.pop()]:
                continue
            else:
                return False
        
        if stack:
            return False
        return True