class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        p_open = p_close = 0

        for c in s:
            if c == '(':
                p_open += 1
            elif c == ')' and p_open > 0:
                p_open -= 1
            else:
                p_close += 1
        
        return p_open + p_close