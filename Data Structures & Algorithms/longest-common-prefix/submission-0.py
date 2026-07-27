class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = min(len(s) for s in strs)

        prefix = ""

        i = 0

        while i < min_len:
            if all(s[i] == strs[0][i] for s in strs):
                i += 1
            else:
                return strs[0][:i]

        return strs[0][:min_len]