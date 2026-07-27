class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_left = height[l]
        max_right = height[r]
        area = 0
        while l < r:
            if max_left <= max_right:
                l += 1
                max_left = max(max_left, height[l])
                a = max_left - height[l]
            else:
                r -= 1
                max_right = max(max_right, height[r])
                a = max_right - height[r]
            if a > 0:
                area += a

        return area