class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        q = deque() # We are going to be appending rotten oranges
        time = fresh = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r,c])
        
        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        while q and fresh > 0:
            q_len = len(q)
            for i in range(q_len):
                r, c = q.popleft()
                # going through all directions
                for dr, dc in directions:
                    row, col = dr + r, dc + c
                    #check is in bounds
                    if row < 0 or row == ROWS or col < 0 or col == COLS:
                        continue
                    if grid[row][col] == 1: # if fresh orange
                        q.append([row, col])
                        grid[row][col] = 2
                        fresh -= 1
            time += 1
        return time if not fresh else -1