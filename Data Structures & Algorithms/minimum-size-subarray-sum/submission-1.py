class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        window = 0
        min_window = float('inf')
        for r in range(len(nums)):
            window += nums[r]
            while window >= target:
                min_window = min(min_window, r - l + 1)
                window -= nums[l]
                l += 1
        
        return min_window if min_window != float('inf') else 0