class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i, c in enumerate(s):
            if c != "]":
                stack.append(c)
            else:
                sub = ""
                while stack[-1] != "[":
                    sub = stack.pop() + sub
                stack.pop()
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k 
                stack.append(int(k) * sub)

        return "".join(stack)