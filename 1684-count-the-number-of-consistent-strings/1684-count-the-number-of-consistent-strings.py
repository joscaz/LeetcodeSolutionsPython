class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = len(words)
        for word in words:
            for i in range(len(word)):
                if word[i] not in allowed:
                    count -= 1
                    break
        return count