class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hm_s = {}
        hm_t = {}

        for letter in s:
            if letter not in hm_s:
                hm_s[letter] = 1
            
            else:
                hm_s[letter] += 1
        
        for letter in t:
            if letter not in hm_t:
                hm_t[letter] = 1
            
            else:
                hm_t[letter] += 1
        
        return hm_t == hm_s
        