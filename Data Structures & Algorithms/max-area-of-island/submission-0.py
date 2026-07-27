class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        max_area = 0

        def backtrack(r, c):
            if not 0 <= r < ROW or not 0 <= c < COL or grid[r][c] == 0:
                return 0 
            grid[r][c] = 0
            return 1 + backtrack(r + 1, c) + backtrack(r - 1, c) + backtrack(r, c + 1) + backtrack(r, c - 1)

        for r in range(ROW):
            for c in range(COL):
                local_area = backtrack(r, c)
                max_area = max(local_area, max_area)
        
        return max_area