class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        hm_s = {}
        hm_t = {}
        for let in s:
            if let not in hm_s:
                hm_s[let] = 0
            hm_s[let] += 1
        
        for let in t:
            if let not in hm_t:
                hm_t[let] = 0
            hm_t[let] += 1
        
        if hm_s == hm_t:
            return True
        
        return False