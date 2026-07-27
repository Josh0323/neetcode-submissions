class Solution:
    def minEnd(self, n: int, x: int) -> int:
        result = x

        i_x = 1
        i_n = 1

        while i_n < n:
            if i_x & x == 0:
                if i_n & (n - 1):
                    result |= i_x
                i_n = i_n << 1
            i_x = i_x << 1
        
        return result