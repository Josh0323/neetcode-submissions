class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_count, s2_count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1
        
        matches = 0
        for c1, c2 in zip(s1_count, s2_count):
            if c1 == c2:
                matches += 1
        
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            i = ord(s2[r]) - ord('a')
            s2_count[i] += 1
            if s2_count[i] == s1_count[i]:
                matches += 1
            elif s2_count[i] == s1_count[i] + 1:
                matches -= 1

            j = ord(s2[r - len(s1)]) - ord('a')           
            s2_count[j] -= 1
            if s2_count[j] == s1_count[j]:
                matches += 1
            elif s2_count[j] == s1_count[j] - 1:
                matches -= 1
            
        return matches == 26