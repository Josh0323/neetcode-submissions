class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        
        def dfs(i, com):
            if i > n:
                if len(com) == k:
                    result.append(com.copy())
                return
            com.append(i)
            dfs(i + 1, com)
            com.pop()
            dfs(i + 1, com)

        dfs(1, [])
        return result