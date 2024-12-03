class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        space_ptr = 0
        new_str = ""

        for i in range(len(s)):
            if space_ptr < len(spaces) and i == spaces[space_ptr]:
                new_str += ' '
                new_str += s[i]
                space_ptr += 1
            else:
                new_str += s[i]
            
        return new_str