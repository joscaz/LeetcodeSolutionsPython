class Solution:
    def compress(self, chars: List[str]) -> int:
        i = j = 0
        
        while i < len(chars):
            char = chars[i]
            count = 0
            
            while i < len(chars) and chars[i] == char:
                count += 1
                i += 1
            
            chars[j] = char
            j += 1
            
            if count > 1:
                for c in str(count):
                    chars[j] = c
                    j += 1
        
        return j