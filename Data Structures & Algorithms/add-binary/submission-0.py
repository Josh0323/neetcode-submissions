class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        carry = 0

        i, j = len(a) - 1, len(b) - 1

        while i >= 0 or j >= 0 or carry > 0:
            a_num = int(a[i]) if i >= 0 else 0
            b_num = int(b[j]) if j >= 0 else 0
            
            total = a_num + b_num + carry
            result.append(total % 2)
            carry = total // 2

            i -= 1
            j -= 1
        result.reverse()
        return ''.join(map(str, result))