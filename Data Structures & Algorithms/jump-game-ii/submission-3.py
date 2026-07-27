class Solution:
    def jump(self, nums: List[int]) -> int:
        
        def dfs(i):
            if i >= len(nums) - 1:
                return 0
            
            if nums[i] == 0:
                return 2000
            
            result = len(nums)
            for j in range(1, nums[i] + 1):
                result = min(result, 1 + dfs(i + j))
            
            return result
        
        return dfs(0)