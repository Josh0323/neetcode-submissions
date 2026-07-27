class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = None

        front, back = 0, 0

        while front < len(nums):
            while front < len(nums) and prev == nums[front]:
                front += 1
            if front == len(nums):
                return back
            nums[back] = nums[front]
            prev = nums[front]
            front += 1
            back += 1

        return back