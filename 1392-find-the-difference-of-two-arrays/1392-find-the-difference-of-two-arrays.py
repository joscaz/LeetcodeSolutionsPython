class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans = []
        cur1 = []
        cur2 = []

        for num in nums1:
            if num not in nums2 and num not in cur1:
                cur1.append(num)
        for num in nums2:
            if num not in nums1 and num not in cur2:
                cur2.append(num)
            
        ans.append(cur1)
        ans.append(cur2)

        return ans