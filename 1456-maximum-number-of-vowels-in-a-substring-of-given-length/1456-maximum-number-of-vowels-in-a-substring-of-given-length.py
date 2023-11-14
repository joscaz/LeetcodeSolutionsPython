class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        max_vowels = 0
        cur_vow = 0
        l, r = 0, k
        
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        for i in range(k):
            if s[i] in vowels:
                cur_vow += 1
                
        max_vowels = cur_vow
        
        while r < len(s):
            
            if s[l] in vowels:
                cur_vow -= 1
            
            if s[r] in vowels: 
                cur_vow += 1
                
            max_vowels = max(max_vowels, cur_vow)
            
            l += 1
            r += 1
        
        return max_vowels