class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def dfs(i, cur):
            if len(cur) == k:
                result.append(cur.copy())
                return

            if i > n:
                return

            cur.append(i)
            dfs(i + 1, cur)
            cur.pop()
            dfs(i + 1, cur)
        
        dfs(1, [])
        return result