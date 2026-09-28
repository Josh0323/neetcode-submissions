class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        def dfs(i, cur):
            if i == len(nums):
                result.append(cur.copy())
                return
            
            cur.append(nums[i])
            dfs(i + 1, cur)

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            cur.pop()
            dfs(i + 1, cur)

        dfs(0, [])
        return result

            