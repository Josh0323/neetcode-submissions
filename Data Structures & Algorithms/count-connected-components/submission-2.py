class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {node: [] for node in range(n)}
        for f, t in edges:
            graph[f].append(t)
            graph[t].append(f)

        result = 0
        visited = set()
        def dfs(node):
            if node in visited:
                return
            visited.add(node)

            for t in graph[node]:
                dfs(t)
            

        for node in range(n):
            if node not in visited:
                dfs(node)
                result += 1
        
        return result
