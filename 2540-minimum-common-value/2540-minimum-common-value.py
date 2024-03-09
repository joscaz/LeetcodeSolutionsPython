class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        minNum = float("inf")

        difference = set(nums1).intersection(set(nums2))

        for item in difference:
            if item < minNum:
                minNum = item

        return -1 if minNum == float("inf") else minNum