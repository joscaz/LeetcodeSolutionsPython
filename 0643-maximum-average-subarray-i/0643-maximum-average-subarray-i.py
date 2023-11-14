class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        suma = 0
        initial, end = 0, k

        for i in range(k):
            suma += nums[i]
        
        max_sum = suma

        while end < len(nums):
            suma -= nums[initial]
            initial += 1

            suma += nums[end]
            end += 1

            max_sum = max(max_sum, suma)
        
        return max_sum / k