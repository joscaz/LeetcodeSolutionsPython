class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        islands = 0
        visited = set()

        def dfs(row, col):
            if row < 0 or row == ROWS or col < 0 or col == COLS or (row, col) in visited or grid[row][col] == '0':
                return 0
            
            visited.add((row, col))

            return (dfs(row+1, col) + dfs(row-1, col) + dfs(row, col+1) + dfs(row, col-1))
        
        for i in range(ROWS):
            for j in range(COLS):
                if (i, j) not in visited and grid[i][j] == '1':
                    islands += 1
                    dfs(i, j)
        return islands