class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if not arr:
            return None
        nums = sorted(arr)
        hm = {}
        rank = 1
        ans = []

        hm[nums[0]] = rank

        for i in range(1, len(nums)):
            if nums[i] not in hm and nums[i] > nums[i-1]:
                rank += 1
                hm[nums[i]] = rank

        for num in arr:
            ans.append(hm[num])
        return ans