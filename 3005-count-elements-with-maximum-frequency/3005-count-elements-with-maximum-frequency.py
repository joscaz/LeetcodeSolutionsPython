class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        hm = {}
        maxVal = 0
        total = 0

        for num in nums:
            if num not in hm:
                hm[num] = 0
            hm[num] += 1

        for item in hm.values():
            if maxVal < item:
                total = 0
                maxVal = item
                total += item
            
            elif maxVal == item:
                total += item
            
            else:
                continue
        return total