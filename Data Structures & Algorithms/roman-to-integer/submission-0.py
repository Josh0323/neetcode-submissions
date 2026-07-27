class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        result = 0
        for i, c in enumerate(s):
            cur = roman[c]
            if i < len(s) - 1:
                if (c == 'I' and (s[i + 1] == 'V' or s[i + 1] == 'X')) or \
                    (c == 'X' and (s[i + 1] == 'L' or s[i + 1] == 'C')) or \
                    (c == 'C' and (s[i + 1] == 'D' or s[i + 1] == 'M')):
                    cur *= -1
            
            result += cur
        
        return result