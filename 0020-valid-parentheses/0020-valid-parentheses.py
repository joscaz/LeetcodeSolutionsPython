class Solution:
    def isValid(self, s: str) -> bool:
        symbols = {'(':')', '[':']', '{':'}'}
        stack = deque()
        
        for c in s:
            if c in symbols:
                stack.appendleft(c)
            elif stack and c == symbols[stack.popleft()]:
                continue
            else:
                return False
        return True if not stack else False
        '''
        stack = (
        symbols[]
        '''