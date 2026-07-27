class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        from collections import Counter
        
        s1_count = Counter(s1)
        s2_count = Counter(s2[:len(s1)])
        l, r = 0, len(s1) - 1
        while r < len(s2):
            if s1_count == s2_count:
                return True
            s2_count[s2[l]] -= 1
            l, r = l + 1, r + 1
            if r < len(s2):
                s2_count[s2[r]] += 1
                

        return False