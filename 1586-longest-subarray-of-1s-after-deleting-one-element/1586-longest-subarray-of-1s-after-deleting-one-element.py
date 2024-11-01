class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zeros = res = 0

        left = 0
        for right, num in enumerate(nums):
            zeros += 1 - num

            while zeros > 1:
                zeros -= (1 - nums[left]) # Only rest when it's a zero
                left += 1

            res = max(res, right - left)
        
        return res