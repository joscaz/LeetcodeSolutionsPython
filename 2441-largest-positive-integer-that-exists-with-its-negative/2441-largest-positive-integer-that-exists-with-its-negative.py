class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        ans = None
        curr = 0
        for num in nums:
            if num > 0 and num > curr and -num in nums:
                curr = num
                ans = num
        
        if not ans:
            return -1
        return ans 