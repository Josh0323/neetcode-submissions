class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for f, t, p in flights:
            adj[f].append((t, p))

        min_heap = [(p, t, 1) for t, p in adj[src]]
        visited = set()

        while min_heap:
            p, s, cur_k = heapq.heappop(min_heap)

            if s == dst:
                return p
            
            if cur_k > k:
                continue
            
            visited.add(s)
            for t, tp in adj[s]:
                if t not in visited:
                    heapq.heappush(min_heap, (tp + p, t, cur_k + 1))
        
        return -1
        
