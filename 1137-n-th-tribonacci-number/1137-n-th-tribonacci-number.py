class Solution:
    def tribonacci(self, n: int) -> int:
        one, two, three = 0, 1, 1

        if n == 0:
            return one
        
        if n == 1 or n == 2:
            return two

        for _ in range(3, n + 1):
            temp = one + two + three
            one, two, three = two, three, temp
        
        return three