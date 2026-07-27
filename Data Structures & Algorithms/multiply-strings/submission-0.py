class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 > num2:
            num1, num2 = num2, num1
        
        
        
        ints = 0
        for i, n1 in enumerate(num1[::-1]):
            int_n1 = int(n1) * (10 ** i)
            for j, n2 in enumerate(num2[::-1]):
                int_n2 = int(n2) * (10 ** j)
                ints += int_n1*int_n2
        
        return str(ints)
