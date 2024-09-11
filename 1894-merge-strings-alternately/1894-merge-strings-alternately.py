class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        newStr = ""

        while i < len(word1) and j < len(word2):
            newStr += word1[i] + word2[j]
            i += 1
            j += 1
        
        newStr += word1[i:] + word2[j:]

        return newStr