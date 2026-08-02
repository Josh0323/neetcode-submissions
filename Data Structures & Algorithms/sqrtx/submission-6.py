class Solution:
    def mySqrt(self, x: int) -> int:
        if 0 <= x <= 1:
            return x
        l, r = 0, x

        while l < r:
            m = l + (r - l) // 2
            sqrt = m * m
            if sqrt <= x:
                l = m + 1
            else:
                r = m
        
        return l - 1