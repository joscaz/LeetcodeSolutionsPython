class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hm1 = {}
        hm2 = {}

        for c in s:
            if c not in hm1:
                hm1[c] = 0
            hm1[c] += 1
             # hm1.get(c, 0) + 1

        for c in t:
            if c not in hm2:
                hm2[c] = 0
            hm2[c] += 1
            # hm2.get(c, 0) + 1

        return hm1 == hm2