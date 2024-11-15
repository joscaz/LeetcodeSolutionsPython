class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sorting the array will make it easier
        # be aware of duplicates
        nums.sort()
        '''
        [-4, -1, -1, 0, 1, 2]
        '''
        ans = []

        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = len(nums)-1
            while j < k:
                cur_triplet = [nums[i], nums[j], nums[k]]
                op = nums[i] + nums[j] + nums[k]
                if op == 0:
                    ans.append(cur_triplet)
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1
                    j += 1
                    k -= 1
                elif op > 0:
                    k -= 1
                else:
                    j += 1
        return ans