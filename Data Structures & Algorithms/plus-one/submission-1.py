class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:


        digits.reverse()
        for i, d in enumerate(digits):
            if d < 9:
                digits[i] += 1
                return digits[::-1]
            digits[i] = 0
        return [1] + digits[::-1]
