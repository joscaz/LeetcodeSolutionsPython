class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hm_s = {}
        hm_t = {}

        for word in s:
            if word not in hm_s:
                hm_s[word] = 0
            hm_s[word] += 1
        
        for word in t:
            if word not in hm_t:
                hm_t[word] = 0
            hm_t[word] += 1

        return hm_s == hm_t