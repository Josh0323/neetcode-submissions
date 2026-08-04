class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        available = []
        pending = []
        
        for i, (e, q) in enumerate(tasks):
            heapq.heappush(pending, (e, q, i))
        
        time = 0
        result = []
        while pending or available:
            while pending and pending[0][0] <= time:
                e, q, i = heapq.heappop(pending)
                heapq.heappush(available, (q, i))

            if not available:
                time = pending[0][0]
                continue
            p, i = heapq.heappop(available)
            time += p
            result.append(i)
        
        return result