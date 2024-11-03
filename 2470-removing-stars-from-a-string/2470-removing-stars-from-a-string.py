class Solution:
    def removeStars(self, s: str) -> str:
        stack = deque()

        i = 0

        for c in s:
            if c == '*':
                stack.pop()
            else:
                stack.append(c)
        
        return ''.join(stack)