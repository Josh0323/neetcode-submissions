class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0 or len(s) == 1:
            return len(s)

        l, r = 0, 1
        max_len = 0
        seen = set()
        seen.add(s[l])
        while r < len(s):
            if s[r] not in seen:
                max_len = max(r - l + 1, max_len)
                seen.add(s[r])
                r += 1
            else:
                seen.remove(s[l])
                l += 1
                
        
        return max_len