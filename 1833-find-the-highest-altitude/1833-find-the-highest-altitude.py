class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest = 0
        cur_alt = 0

        for alt in gain:
            cur_alt += alt
            highest = max(highest, cur_alt)
        
        return highest