class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        hm = {}

        for num in arr:
            if num not in hm:
                hm[num] = 0
            hm[num] += 1
        
        percent = len(arr)//4
        for key, val in hm.items():
            if val > percent:
                return key
        return -1