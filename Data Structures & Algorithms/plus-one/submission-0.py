class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        result = []

        for d in digits[::-1]:
            result.append( (d + carry) % 10)
            carry = (d + carry) // 10

        if carry != 0:
            result.append(carry)

        result.reverse()

        return result