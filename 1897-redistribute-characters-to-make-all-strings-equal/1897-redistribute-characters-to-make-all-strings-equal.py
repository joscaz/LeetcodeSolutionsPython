class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        count_of_char = {}

        for word in words:
            for letter in word:
                if letter not in count_of_char:
                    count_of_char[letter] = 0
                count_of_char[letter] += 1
        
        for item in count_of_char:
            if count_of_char[item] % len(words) == 0:
                continue

            else:
                return False

        return True 