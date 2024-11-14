class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hm1 = {}
        hm2 = {}

        for i in range(len(s)):
            if s[i] not in hm1:
                hm1[s[i]] = 0
            hm1[s[i]] += 1

            if t[i] not in hm2:
                hm2[t[i]] = 0
            hm2[t[i]] += 1
        
        return hm1 == hm2