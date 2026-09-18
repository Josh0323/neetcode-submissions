class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        min_heap, max_heap = [], []
        for i, c in enumerate(capital):
            heapq.heappush(min_heap, (c, i))
        
        while k > 0:
            while min_heap and min_heap[0][0] <= w:
                c, i = heapq.heappop(min_heap)
                heapq.heappush_max(max_heap, (profits[i], i))
            if not max_heap:
                break
            p, i = heapq.heappop_max(max_heap)
            w += p
            k -= 1
        
        return w