class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i = 0
        j = math.floor(math.sqrt(c))
        
        while i <= j:
            formula = (i * i) + (j * j)
            if formula == c:
                return True
            elif formula > c:
                j -= 1
            else:
                i += 1
        return False

"""


"""