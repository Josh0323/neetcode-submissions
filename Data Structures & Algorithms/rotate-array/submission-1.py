class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start, count = 0, 0

        while count < len(nums):
            current = start
            prev = nums[start]
            while True:
                next_i = (current + k) % len(nums)
                nums[next_i], prev = prev, nums[next_i]
                count += 1
                current = next_i
                if current == start:
                    break
            start += 1
