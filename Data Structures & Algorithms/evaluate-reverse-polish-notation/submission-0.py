class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ariths = {
            "+": lambda a, b: a + b,
            "*": lambda a, b: a * b,
            "-": lambda a, b: a - b,
            "/": lambda a, b: int(a / b)
        }

        stack = []
        
        for t in tokens:
            if t in ariths:
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(str(ariths[t](a, b)))
            else:
                stack.append(t)

        return int(stack[-1])