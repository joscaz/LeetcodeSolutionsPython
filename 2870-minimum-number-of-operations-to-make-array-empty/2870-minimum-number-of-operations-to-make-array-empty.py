class Solution:
    def minOperations(self, nums: List[int]) -> int:

        operations = 0
        hm = {}
        
        for num in nums:
            if num not in hm:
                hm[num] = 0
            hm[num] += 1

        for item in hm:
            if hm[item] == 1:
                return -1
            
            operations += ceil(hm[item] / 3)
        
        return operations
