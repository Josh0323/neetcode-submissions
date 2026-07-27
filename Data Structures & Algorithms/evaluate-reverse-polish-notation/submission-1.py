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
                b = stack.pop()
                a = stack.pop()
                stack.append(ariths[t](a, b))
            else:
                stack.append(int(t))

        return int(stack[-1])