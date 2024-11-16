class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        symbols = {'+', '/', '-', '*'}

        for c in tokens:
            if c not in symbols:
                stack.append(c)
            else:
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                res = self.mathOperation(c, num1, num2)
                stack.append(str(res))

        return int(stack[-1])
    
    def mathOperation(self, operation, num1, num2):
        res = 0
        if operation == "/":
            res = int(num2 / num1)
        elif operation == "+":
            res = num2 + num1
        elif operation == "-":
            res = num2 - num1
        elif operation == "*":
            res = num2 * num1
        
        return res