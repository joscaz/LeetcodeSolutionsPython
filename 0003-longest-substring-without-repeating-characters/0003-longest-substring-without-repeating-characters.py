class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, end = 0, 1
        longest = 0

        while end < len(s):
            if s[end] in s[start:end]:
                start += 1
            else:
                end += 1
            longest = max(longest, end - start)
        
        return longest
        