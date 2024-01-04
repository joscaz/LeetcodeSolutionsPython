class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        hm = {}
        curr = 0
        i = 0
        ans = 0

        for row in bank:
            for num in row:
                if num == "1":
                    curr += 1
            
            if curr == 0:
                continue
            
            else:
                hm[i] = curr
                i += 1
                curr = 0
        
        if len(hm) < 2:
            return 0
        
        else:
            for i in range(1, len(hm)):
                ans += hm[i-1] * hm[i]
            
            return ans