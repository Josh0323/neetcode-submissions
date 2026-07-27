class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = defaultdict(list)
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append((dist, j))
                adj[j].append((dist, i))
        
        visited = set()
        min_heap = [(0, 0)]
        cost = 0

        while len(visited) < len(points):
            c, n = heapq.heappop(min_heap)
            if n in visited:
                continue
            
            visited.add(n)
            cost += c
            for nei_cost, nei in adj[n]:
                if nei not in visited:
                    heapq.heappush(min_heap, (nei_cost, nei))

        return cost