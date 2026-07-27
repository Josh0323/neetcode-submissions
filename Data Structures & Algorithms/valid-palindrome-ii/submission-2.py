class Solution:
    def validPalindrome(self, s: str) -> bool:
        def subsearch(i, j):
            while i < j:
                while not s[i].isalnum() and i < j:
                    i += 1
                while not s[j].isalnum() and i < j:
                    j -= 1
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        
        x, y = 0, len(s) - 1
        skipped = False
        while x < y:
            while not s[x].isalnum() and x < y:
                x += 1
            while not s[y].isalnum() and x < y:
                y -= 1
            if s[x] != s[y]:
                if not skipped:
                    return subsearch(x + 1, y) or subsearch(x, y - 1)
                return False
            x += 1
            y -= 1
        
        return True