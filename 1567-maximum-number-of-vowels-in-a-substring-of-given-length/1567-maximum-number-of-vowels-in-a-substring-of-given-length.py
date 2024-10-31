class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        max_cnt = cur_cnt = 0
        vowels = {'a', 'e', 'i', 'o', 'u'}

        for i in range(k):
            if s[i] in vowels:
                cur_cnt += 1
        
        max_cnt = cur_cnt

        for right in range(k, len(s)):
            if s[right-k] in vowels:
                cur_cnt -= 1
            
            if s[right] in vowels:
                cur_cnt += 1
            
            max_cnt = max(cur_cnt, max_cnt)
        
        return max_cnt