class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        def dfs(i, cur):
            if i == len(nums) - 1 and cur == target:
                return 1
            if i + 1 >= len(nums):
                return 0
            return dfs(i + 1, nums[i+1] + cur) + dfs(i + 1, -nums[i+1] + cur)

        
        return dfs(0, nums[0]) + dfs(0, -nums[0])