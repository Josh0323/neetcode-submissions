class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        def dfs(ns):
            if len(ns) == 2:
                return 0

            max_coins = 0
            for i in range(1, len(ns) - 1):
                coins = ns[i - 1] * ns[i] * ns[i + 1]
                coins += dfs(ns[:i] + ns[i + 1:])
                max_coins = max(max_coins, coins)
            
            return max_coins
        return dfs(nums)