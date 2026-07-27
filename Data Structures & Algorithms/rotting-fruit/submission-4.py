class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        q = collections.deque()
        fresh, time = 0, 0

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while fresh > 0 and q:
            length = len(q)

            for _ in range(length):
                r, c = q.popleft()

                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if 0 <= row < ROW and 0 <= col < COL \
                        and grid[row][col] == 1:
                        grid[row][col] = 2
                        fresh -= 1
                        q.append((row, col))
                
            time += 1
        
        return time if fresh == 0 else -1
                
