class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = None

        front, back = 0, 0

        while front < len(nums):
            nums[back] = nums[front]
            while front < len(nums) and nums[back] == nums[front]:
                front += 1
            back += 1
        return back