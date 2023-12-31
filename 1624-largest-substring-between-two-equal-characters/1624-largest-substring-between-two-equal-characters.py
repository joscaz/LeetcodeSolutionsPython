class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        hm = {}
        max_len = -1

        for i in range(len(s)):
            if s[i] not in hm:
                hm[s[i]] = i
            
            else:
                max_len = max(max_len, i - hm[s[i]])
        
        return max_len if max_len == -1 else max_len - 1

        