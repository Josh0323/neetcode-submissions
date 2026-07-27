class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = defaultdict(int)
        for c in s:
            s_dict[c] += 1
        
        for c in t:
            s_dict[c] -= 1

        for v in s_dict.values():
            if v != 0:
                return False
        
        return True