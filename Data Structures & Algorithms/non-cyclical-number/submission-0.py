class Solution:
    def isHappy(self, n: int) -> bool:
        def ncn(num):
            result = 0
            for i in str(num):
                result += int(i) ** 2
            return result

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = ncn(n)
        
        return n == 1