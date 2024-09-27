class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        '''
        [-4,-1,-1,0,1,2]

        i = 0
          low = 1
          high = 5
          curVal = 
        '''
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            low, high = i+1, len(nums)-1
            curVal = nums[i]
            while low < high:
                operation = curVal + nums[low] + nums[high]
                curTriplet = [nums[i], nums[low], nums[high]]
                if operation == 0:
                    ans.append(curTriplet)
                    while low < high and nums[low] == nums[low+1]:
                        low += 1
                    while low < high and nums[high] == nums[high-1]:
                        high -= 1
                    low += 1
                    high -= 1
                elif operation > 0:
                    high -= 1
                else:
                    low += 1
        return ans