class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_mat = defaultdict(list)

        for f, t, w in times:
            adj_mat[f].append((w, t))

        mh = [(0, k)]
        heapq.heapify(mh)
        visited = set()
        t = 0

        while mh:
            w, node = heapq.heappop(mh)
            if node in visited:
                continue
            
            visited.add(node)
            t = w

            for w2, node2 in adj_mat[node]:
                if node2 not in visited:
                    heapq.heappush(mh, (w + w2, node2))
        
        return t if len(visited) == n else -1