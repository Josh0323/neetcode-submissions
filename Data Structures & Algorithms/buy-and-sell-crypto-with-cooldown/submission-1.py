class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dfs(i, p):
            if i >= len(prices):
                return 0

            if (i, p) in memo:
                return memo[(i, p)]

            if p != -1:
                memo[(i, p)] = max(prices[i] - p + dfs(i + 2, -1), dfs(i + 1, p))
            else:
                memo[(i, p)] = max(dfs(i + 1, prices[i]), dfs(i + 1, -1))
            
            return memo[(i, p)]
        
        return dfs(0, -1)