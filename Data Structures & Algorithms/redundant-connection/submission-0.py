class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj_mat = {node: [] for node in range(1, len(edges) + 1)}

        visited = set()
        def dfs(node, parent):
            if node in visited:
                return False

            visited.add(node)
            for t in adj_mat[node]:
                if t == parent:
                    continue
                if not dfs(t, node):
                    return False
            
            return True
        
        for f, t in edges:
            adj_mat[f].append(t)
            adj_mat[t].append(f)
            visited.clear()
            if not dfs(f, -1):
                return [f, t]

