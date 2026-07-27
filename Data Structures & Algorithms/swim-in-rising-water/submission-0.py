class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        directions = [(0,-1), (0,1), (1, 0),(-1, 0)]
        min_heap = [(grid[0][0], 0, 0)]
        visited = set()

        while min_heap:
            t, r, c = heapq.heappop(min_heap)

            if r == len(grid) - 1 and c == len(grid[0]) - 1:
                return t
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if not 0 <= nr < len(grid) or \
                not 0 <= nc < len(grid[0]) or \
                (nr, nc) in visited:
                    continue
                
                visited.add((nr, nc))
                heapq.heappush(min_heap, (max(t, grid[nr][nc]), nr, nc))

        