class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        
        #2,3,3,5
        nums.sort()
        l, r = 0, len(nums) - 1
        max_sum = 0

        while l < r:
            max_sum = max(nums[l] + nums[r], max_sum)
            l += 1
            r -= 1
        
        return max_sum