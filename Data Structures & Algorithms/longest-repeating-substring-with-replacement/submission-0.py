class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        repeats = defaultdict(int)

        l, res = 0, 0
        for r in range(len(s)):
            repeats[s[r]] += 1
            if (r - l + 1) - max(repeats.values()) > k:
                repeats[s[l]] -= 1
                l += 1
            res = max(r - l + 1, res)
        
        return res