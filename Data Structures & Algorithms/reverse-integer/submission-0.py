class Solution:
    def reverse(self, x: int) -> int:
        def recursive(n, result):
            if n == 0:
                return result
            
            result = result * 10 + n % 10
            return recursive(n // 10, result)

        sign = 1 if x >=0 else -1
        result = recursive(abs(x), 0) * sign

        if result > (1 << 31) - 1 or result < -(1 << 31):
            return 0
        return result