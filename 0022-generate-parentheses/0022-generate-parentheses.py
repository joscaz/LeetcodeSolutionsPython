class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Three conditions
        # 1. if open == closed == n return
        # 2. if open parentheses < n add open par
        # 3. if close parentheses < open add closing par

        stack = []
        res = []

        def backtrack(openN, closeN):
            if openN == closeN == n:
                res.append("".join(stack))
                return
            if openN < n:
                stack.append('(')
                backtrack(openN+1, closeN)
                stack.pop()
            if closeN < openN:
                stack.append(')')
                backtrack(openN, closeN+1)
                stack.pop()
        backtrack(0,0)
        return res