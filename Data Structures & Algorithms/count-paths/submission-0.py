class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[-1] * n for _ in range(m)]

        def dfs(x, y):
            if x == m - 1 and y == n - 1:
                return 1
            
            if not 0 <= x < m or not 0 <= y < n:
                return 0
            
            if memo[x][y] != -1:
                return memo[x][y]
            
            memo[x][y] = dfs(x + 1, y) + dfs(x, y + 1)
            
            return memo[x][y]
        
        return dfs(0, 0)
        