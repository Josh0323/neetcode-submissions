class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        result = 0
        ROW, COL = len(grid), len(grid[0])

        def backtrack(r, c):
            if not 0 <= r < ROW or not 0 <= c < COL or grid[r][c] == "0":
                return

            grid[r][c] = "0"

            backtrack(r + 1, c) 
            backtrack(r - 1, c) 
            backtrack(r, c + 1) 
            backtrack(r, c - 1)


        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == "1":
                    result += 1
                    backtrack(r, c)

        return result 