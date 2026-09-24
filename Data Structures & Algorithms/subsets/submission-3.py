class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        for i in range(1 << len(nums)):
            subset = [nums[j] for j in range(len(nums)) if i & (1 << j)]
            result.append(subset)
        
        return result