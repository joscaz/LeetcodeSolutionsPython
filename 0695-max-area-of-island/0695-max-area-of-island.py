class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        area = 0

        def dfs(row, col):
            if row < 0 or row == ROWS or col < 0 or col == COLS or (row, col) in visited or grid[row][col] == 0:
                return 0
            
            visited.add((row, col))

            return (1 + dfs(row-1, col) + dfs(row+1, col) + dfs(row, col-1) + dfs(row, col+1))

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                area = max(area, dfs(i, j))
        return area