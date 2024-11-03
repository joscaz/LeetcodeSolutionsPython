class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        for i in range(len(s)):
            if s[i] != ']':
                stack.append(s[i])
            
            else:
                new_str = ""
                while stack[-1] != '[':
                    new_str = stack.pop() + new_str
                stack.pop() # remove '['
                
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(int(k) * new_str)

        return ''.join(stack)