class Solution:
    def firstUniqChar(self, s: str) -> int:
        hm = defaultdict(int)

        for c in s:
            hm[c] += 1

        for i in range(len(s)):
            if hm[s[i]] == 1:
                return i
        
        return -1