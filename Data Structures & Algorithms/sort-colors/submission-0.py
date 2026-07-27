class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        count_one, count_two = 0, 0

        for i in nums:
            if i == 1:
                count_one += 1
            if i == 2:
                count_two += 1
        
        i = 0
        while i < len(nums):
            if i < len(nums) - (count_one + count_two):
                nums[i] = 0
            elif count_one != 0:
                nums[i] = 1
                count_one -= 1
            elif count_two != 0:
                nums[i] = 2
                count_two -= 1
            i += 1
        
        
            