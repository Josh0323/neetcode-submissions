class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        result = 0
        for i in range(32):
            if not (left >> i) & 1:
                continue
            
            remain = left % (1 << (i + 1))
            diff = (1 << (i + 1)) - remain

            if right - left < diff:
                result |= (1 << i)
        return result