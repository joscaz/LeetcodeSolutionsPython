class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []

        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = len(nums)-1
            while j < k:
                op = nums[i] + nums[j] + nums[k]
                cur_triplet = [nums[i], nums[j], nums[k]]
                if op == 0:
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1
                    j += 1
                    k -= 1
                    ans.append(cur_triplet)
                elif op > 0:
                    k -= 1
                else:
                    j += 1
        return ans