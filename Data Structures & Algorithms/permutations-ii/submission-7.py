class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        perms = []
        
        def backtrack(idx):
            if idx == len(nums):
                perms.append(nums.copy())
                return

            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[idx]:
                    continue

                nums[idx], nums[i] = nums[i], nums[idx]
                backtrack(idx + 1) 
            
            for i in range(len(nums) - 1, idx, -1):
                nums[i], nums[idx] = nums[idx], nums[i]
        
        backtrack(0)
        return perms