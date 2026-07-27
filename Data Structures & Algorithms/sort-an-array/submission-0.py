class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        pivot = nums[len(nums) // 2]

        left = [l for l in nums if l < pivot]
        mid = [m for m in nums if m == pivot]
        right = [r for r in nums if r > pivot]
        
        return self.sortArray(left) + mid + self.sortArray(right)