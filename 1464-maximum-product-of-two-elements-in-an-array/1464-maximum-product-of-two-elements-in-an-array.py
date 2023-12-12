class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_num = 0

        for i in range(len(nums)):
            for j in range(len(nums)):
                formula = ((nums[i]-1)*(nums[j]-1))
                if i == j:
                    continue
                if formula > max_num:
                    max_num = formula

        return max_num