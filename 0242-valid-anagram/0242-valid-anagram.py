class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hm1 = defaultdict(int)
        hm2 = defaultdict(int)

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            hm1[s[i]] += 1
            hm2[t[i]] += 1

        return hm1 == hm2