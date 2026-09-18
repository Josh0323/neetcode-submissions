class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        indices = list(range(len(profits)))
        indices.sort(key=lambda i : capital[i])

        max_prof = []
        i = 0
        for _ in range(k):
            while i < len(profits) and capital[indices[i]] <= w:
                heapq.heappush_max(max_prof, profits[indices[i]])
                i += 1
            if not max_prof:
                break
            w += heapq.heappop_max(max_prof)
        
        return w