class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROW, COL = len(grid), len(grid[0])
        visited = set()
        def dfs(r, c, incre):
            if not 0 <= r < ROW or not 0 <= c < COL \
            or grid[r][c] == -1 or (r, c) in visited \
            or incre > grid[r][c] and grid[r][c] < sys.maxsize:
                return
            
            visited.add((r, c))
            if incre <= grid[r][c]:
                grid[r][c] = incre

            incre += 1
            
            dfs(r + 1, c, incre)
            dfs(r - 1, c, incre)
            dfs(r, c + 1, incre)
            dfs(r, c - 1, incre)
            visited.remove((r, c))

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 0:
                    dfs(r, c, 0)