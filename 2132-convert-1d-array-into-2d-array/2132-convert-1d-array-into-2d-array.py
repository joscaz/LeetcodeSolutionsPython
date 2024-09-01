class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) > (m * n) or len(original) < (m*n): # 1 > 2? NO
            return []
        ans = []
        curr = []
        i, j = 0, 0
        idx_original = 0
        
        while i < m:
            curr = []
            while j < n:
                curr.append(original[idx_original])
                idx_original += 1
                j += 1
            j = 0
            i += 1
            ans.append(curr)

        return ans