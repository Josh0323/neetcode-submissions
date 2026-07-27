class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)
        
        if n < m:
            m, n = n, m
            str1, str2 = str2, str1
        

        for l in range(m, 0, -1):
            if m % l != 0 or n % l != 0:
                continue
            
            flag = True
            for i in range(n - 1, 0, -1):
                if str1[i % l] != str2[i]:
                    flag = False
                    break

            if flag:
                return str1[:l]

        return ""