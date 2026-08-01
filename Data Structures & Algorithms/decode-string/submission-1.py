class Solution:
    def decodeString(self, s: str) -> str:
        str_stack = []
        k_stack = []
        cur, k = "", 0

        for c in s:
            if c.isdigit():
                k = k * 10 + int(c)
            elif c == "[":
                str_stack.append(cur)
                k_stack.append(k)
                cur, k = "", 0
            elif c == "]":
                cur = str_stack.pop() + cur * k_stack.pop()
            else:
                cur += c
        
        return cur
