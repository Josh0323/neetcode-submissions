class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        from collections import Counter
        
        s1_count = Counter(s1)
        s2_count = Counter(s2[:len(s1)])
        if s1_count == s2_count:
            return True
        for r in range(len(s1), len(s2)):
            s2_count[s2[r - len(s1)]] -= 1
            s2_count[s2[r]] += 1
            if s1_count == s2_count:
                return True

        return False