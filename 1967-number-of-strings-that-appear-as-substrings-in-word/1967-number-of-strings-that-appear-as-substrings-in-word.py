class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        appearances = 0

        for w in patterns:
            if w in word:
                appearances += 1

        return appearances