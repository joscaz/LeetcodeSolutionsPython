class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()

        for i in range(1, len(nums), 2):
            temp = nums[i-1]
            nums[i - 1] = nums[i]
            nums[i] = temp 

        return nums