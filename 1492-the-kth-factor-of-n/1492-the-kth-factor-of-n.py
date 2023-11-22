class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        arr = []
        count = 0

        for i in range(1, n + 1):
            if n % i == 0:
                arr.append(i)
        
        return -1 if k > len(arr) else arr[k - 1]