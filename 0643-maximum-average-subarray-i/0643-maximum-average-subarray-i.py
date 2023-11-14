class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        suma = 0
        l, r = 0, k
        
        for i in range(k):
            suma += nums[i]
        
        max_sum = suma
        
        while r < len(nums):
            suma -= nums[l]
            suma += nums[r]
            
            l += 1
            r += 1
            
            max_sum = max(max_sum, suma)
        
        return max_sum / k