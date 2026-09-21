class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def dfs(i, target):
            if i == len(nums):
                return target
            
            return dfs(i + 1, target ^ nums[i]) + dfs(i + 1, target)
        return dfs(0, 0)