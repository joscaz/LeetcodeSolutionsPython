class Solution:
    def getLucky(self, s: str, k: int) -> int:
        s_to_int = self.stringToInt(s)

        while k > 0:
            result = 0
            for i in range(len(str(s_to_int))):
                result += int(str(s_to_int)[i])
            s_to_int = result
            k -= 1
        
        return result

    def stringToInt(self, s):
        result = ""

        for c in s:
            result += str(ord(c) - ord('a') + 1)
        
        return int(result)