class Solution:
    def removeStars(self, s: str) -> str:
        stack = deque()
        new_string = ""

        i = 0

        while i < len(s):
            if s[i] == '*':
                stack.pop()
            else:
                stack.append(s[i])
            i += 1
        
        return ''.join(stack)