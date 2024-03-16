class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = set("qwertyuiopQWERTYUIOP")
        row2 = set("asdfghjklASDFGHJKL")
        row3 = set("zxcvbnmZXCVBNM")
        ans = []

        for word in words:
            wordSet = set(word)
            if wordSet.issubset(row1) or wordSet.issubset(row2) or wordSet.issubset(row3):
                ans.append(word)

        return ans