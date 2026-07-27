class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        alpha_list = [0] * 26

        for c1, c2 in zip(s, t):
            alpha_list[ord(c1) - ord('a')] += 1
            alpha_list[ord(c2) - ord('a')] -= 1
        
        for a in alpha_list:
            if a != 0:
                return False
        return True