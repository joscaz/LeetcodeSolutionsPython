class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        hm = {}
        maxLen = 0

        for right in range(len(s)):
            
            if s[right] in hm and hm[s[right]] >= left:
                left = hm[s[right]] + 1
            
            hm[s[right]] = right
            curLen = right - left + 1
            maxLen = max(curLen, maxLen)
        
        return maxLen