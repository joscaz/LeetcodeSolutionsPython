class Solution:
    def romanToInt(self, s: str) -> int:
        i = 0
        ans = 0

        romans = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }

        while i < len(s):
            if i == len(s) - 1:
                ans += romans[s[i]]
                i += 1
            
            elif romans[s[i]] < romans[s[i + 1]]:
                ans += romans[s[i + 1]] - romans[s[i]]
                i += 2
            
            else:
                ans += romans[s[i]]
                i += 1
        
        return ans
