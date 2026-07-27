class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)

        prev = 1
        for i in range(len(nums)):
            output[i] *= prev
            prev *= nums[i]
        
        post = 1
        for j in range(len(nums) - 1, -1, -1):
            output[j] *= post
            post *= nums[j]
        
        return output