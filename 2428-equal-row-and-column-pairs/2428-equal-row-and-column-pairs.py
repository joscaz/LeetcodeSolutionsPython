class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        hm = {}

        for row in range(len(grid)):
            cur_row = []
            for col in range(len(grid[0])):
                cur_row.append(grid[row][col])
            
            cur_row = tuple(cur_row)
            if cur_row not in hm:
                hm[cur_row] = 0
            hm[cur_row] += 1

        total = 0

        for i in range(len(grid)):
            cur_col = []
            for j in range(len(grid)):
                cur_col.append(grid[j][i])
            
            if tuple(cur_col) in hm:
                total += hm[tuple(cur_col)]
        
        return total