class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        cur = []
        result = []
        wordDict = set(wordDict)
        def dfs(i):
            if i == len(s):
                result.append(" ".join(cur))
                return
            
            for j in range(i, len(s)):
                word = s[i:j + 1]
                if word in wordDict:
                    cur.append(word)
                    dfs(j + 1)
                    cur.pop()
            
        dfs(0)
        return result