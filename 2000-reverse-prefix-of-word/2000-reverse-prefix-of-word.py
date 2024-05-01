class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word

        list1 = list(word)
        
        for i in range(len(word)):
            if word[i] == ch:
                break
        
        j = 0
        while j <= i:
            temp = list1[i]
            list1[i] = list1[j]
            list1[j] = temp
            j += 1
            i -= 1
        
        return ''.join(list1)