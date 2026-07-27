class Solution:
    def jump(self, nums: List[int]) -> int:
        memo = {}
        def dfs(i):
            if i in memo:
                return memo[i]

            if i >= len(nums) - 1:
                memo[i] = 0
                return 0
            
            if nums[i] == 0:
                memo[i] = 2000
                return 2000
            
            result = len(nums)
            for j in range(1, nums[i] + 1):
                result = min(result, 1 + dfs(i + j))
            memo[i] = result
            return memo[i]
        
        return dfs(0)