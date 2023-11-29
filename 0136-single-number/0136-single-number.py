class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = set()

        for item in nums:
            if item in seen:
                seen.remove(item)
            else:
                seen.add(item)
        
        for res in seen:
            return res