class Solution:
    def pivotInteger(self, n: int) -> int:
        sumI = 0
        sumJ = 0

        if n == 1:
            return 1

        for i in range(1, n + 1):
            sumI += i
            sumJ = 0

            for j in range(i, n + 1):
                sumJ += j

            if sumI == sumJ:
                return i
                        
        return -1