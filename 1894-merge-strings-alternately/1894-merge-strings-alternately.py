class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = j = 0
        new_str = ""

        while i < len(word1) and j < len(word2):
            new_str += word1[i]
            new_str += word2[j]
            i += 1
            j += 1

        new_str += word1[i:]
        new_str += word2[j:]

        return new_str