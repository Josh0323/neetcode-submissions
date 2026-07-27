class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        directions = [(1,0), (-1,0), (0, 1), (0, -1)]
        dp = {}
        def dfs(i, j, prev):
            if not 0 <= i < len(matrix) or not 0 <= j < len(matrix[0]) or matrix[i][j] <= prev:
                return 0
            result = 1
            if (i, j) in dp:
                return dp[(i, j)]
            for dx, dy in directions:
                nx, ny = i + dx, j + dy
                result = max(result, 1 + dfs(nx, ny, matrix[i][j]))
            dp[(i, j)] = result
            return result
        
        ret = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ret = max(ret, dfs(i, j, float('-inf')))
        
        return ret