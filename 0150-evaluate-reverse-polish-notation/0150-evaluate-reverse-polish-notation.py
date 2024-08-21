class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = ('+', '-', '*', '/')

        for c in tokens:
            if c in ops:
                self.mathOperation(stack, c)
            else:
                stack.append(c)
        
        return int(stack[-1])

    
    def mathOperation(self, stack, ch):
        res = 0
        if ch == '+':
            res = int(stack[-2]) + int(stack[-1])
            stack.pop()
            stack.pop()
        elif ch == '-':
            res = int(stack[-2]) - int(stack[-1])
            stack.pop()
            stack.pop()
        elif ch == '*':
            res = int(stack[-2]) * int(stack[-1])
            stack.pop()
            stack.pop()
        elif ch == '/':
            if stack[-1] == '0' or stack[-1] == 0:
                res = 0
            else:
                res = int(stack[-2]) / int(stack[-1])
                if res >= 0 and res < 1:
                    res = 0
            stack.pop()
            stack.pop()
        stack.append(res)
