class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        ans = []

        str_list = map(str, digits)
        str_digit = ''.join(str_list)
        digit = int(str_digit) + 1
        digit = str(digit)
        for i in digit:
            ans.append(i)

        ans = map(int, ans)
        return ans