class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        ans = []
        count = 0

        for c in s:
            if c == '(':
                count += 1
                ans.append(c)
            elif c == ')' and count > 0:
                    ans.append(c)
                    count -= 1
            elif c != ')':
                ans.append(c)
        
        take_out_open = []

        for c in ans[::-1]:
            if c == '(' and count > 0:
                count -= 1
            else:
                take_out_open.append(c)
        
        return ''.join(take_out_open[::-1])