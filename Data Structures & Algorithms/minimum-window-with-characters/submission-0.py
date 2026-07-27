class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ts, win = {}, {}

        for c in t:
            ts[c] = ts.get(c, 0) + 1
            win[c] = 0

        need = len(ts)
        have = 0

        i = 0
        result, result_ind = float("infinity"), [-1, -1]
        for j in range(len(s)):
            cur = s[j]
            if cur in ts:
                win[cur] += 1
                if win[cur] == ts[cur]:
                    have += 1

            while have == need:
                cur_len = j - i + 1
                if cur_len < result:
                    result = cur_len
                    result_ind = [i, j]

                if s[i] in ts:
                    win[s[i]] -= 1
                    if win[s[i]] < ts[s[i]]:
                        have -= 1
                i += 1
        i, j = result_ind
        return s[i:j + 1] if result != float("infinity") else ""