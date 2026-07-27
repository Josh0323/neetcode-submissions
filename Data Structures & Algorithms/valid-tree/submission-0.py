class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        graph = {e : [] for e in range(n)}
        for f, t in edges:
            graph[f].append(t)
            graph[t].append(f)
        
        visited = set()

        def dfs(node, parent):
            if node in visited:
                return False
            
            visited.add(node)
            for t in graph[node]:
                if t == parent:
                    continue
                if not dfs(t, node):
                    return False
            return True
        
        return dfs(0, -1) and len(visited) == n