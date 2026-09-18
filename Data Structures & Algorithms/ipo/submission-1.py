class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        min_cap = [(c, p) for c, p in zip(capital, profits)]
        heapq.heapify(min_cap)

        max_prof = []
        
        for _ in range(k):
            while min_cap and min_cap[0][0] <= w:
                c, p = heapq.heappop(min_cap)
                heapq.heappush_max(max_prof, p)
            if not max_prof:
                break
            w += heapq.heappop_max(max_prof)
        
        return w