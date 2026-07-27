class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = [0] * len(height)
        maxRight = [0] * len(height)

        for i in range(len(height)):
            if i == 0:
                continue
            maxLeft[i] = max(maxLeft[i - 1], height[i - 1])
        
        for i in range(len(height) - 1, -1, -1):
            if i == len(height) - 1:
                continue
            maxRight[i] = max(maxRight[i + 1], height[i + 1])
        
        area = 0

        for i, h in enumerate(height):
            a = min(maxLeft[i], maxRight[i]) - h
            if a > 0:
                area += a
        
        return area