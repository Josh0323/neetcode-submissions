class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)

        prev = nums[0]
        for i in range(1, len(nums)):
            output[i] *= prev
            prev *= nums[i]
        
        post = nums[-1]
        for j in range(len(nums) - 2, -1, -1):
            output[j] *= post
            post *= nums[j]
        
        return output