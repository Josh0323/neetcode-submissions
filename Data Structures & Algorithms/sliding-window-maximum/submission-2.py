class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        cur_heap = [(-n, i)  for i, n in enumerate(nums[:k])]
        heapq.heapify(cur_heap)
        result = [-cur_heap[0][0]]
        
        for r in range(k, len(nums)):
            heapq.heappush(cur_heap, (-nums[r], r))

            while cur_heap[0][1] <= r - k:
                heapq.heappop(cur_heap)
            result.append(-cur_heap[0][0])
        return result