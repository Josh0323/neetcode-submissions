class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        def dfs(i, cur):
            if i == len(nums):
                return target == cur
            return dfs(i + 1, cur + nums[i]) + dfs(i + 1, cur - nums[i])

        
        return dfs(0, 0)