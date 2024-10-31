class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        if len(nums) == 1:
            return nums

        i, j = 0, 1
        while j < len(nums) and i < len(nums):
            if nums[i] == 0 and nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
            
            if nums[i] != 0:
                i += 1

            if nums[j] == 0:
                j += 1
            
        '''
        1 3 0 0 12
        '''