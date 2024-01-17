class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        ocu = {}
        set_ocu = set()

        for num in arr:
            if num not in ocu:
                ocu[num] = 0
            ocu[num] += 1
    
        for val in ocu.values():
            if val in set_ocu:
                return False
            set_ocu.add(val)
        
        return True