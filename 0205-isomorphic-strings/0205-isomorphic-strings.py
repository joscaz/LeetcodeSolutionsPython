class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hm1 = {}
        hm2 = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            letter = s[i]
            if letter not in hm1:
                hm1[letter] = []
            hm1[letter].append(i)
        
        for i in range(len(t)):
            letter = t[i]
            if letter not in hm2:
                hm2[letter] = []
            
            hm2[letter].append(i)

        return list(hm1.values()) == list(hm2.values())
