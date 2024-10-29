class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        i, j = 0, len(s)-1
        rev_string = list(s)

        while i < j:
            if rev_string[i] in vowels and rev_string[j] in vowels:
                rev_string[i], rev_string[j] = rev_string[j], rev_string[i]
                i += 1
                j -= 1
            
            if rev_string[i] not in vowels:
                i += 1
            if rev_string[j] not in vowels:
                j -= 1

        return ''.join(rev_string)