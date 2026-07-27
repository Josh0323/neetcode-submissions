class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        memo = {}
        def dfs(i, flag):
            if i == len(nums):
                return 0 if flag else -1e6
            if (i, flag) in memo:
                return memo[(i, flag)]
            if flag:
                memo[(i, flag)] = max(0, nums[i] + dfs(i + 1, True))
            else:
                memo[(i, flag)] = max(dfs(i + 1, False), nums[i] + dfs(i + 1, True))
            return memo[(i, flag)]            

        return dfs(0, False)