class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        stones = [-i for i in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            x, y = -heapq.heappop(stones), -heapq.heappop(stones)
            heapq.heappush(stones, -abs(x - y))
        
        return -stones[0]