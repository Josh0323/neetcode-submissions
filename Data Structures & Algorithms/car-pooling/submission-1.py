class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda x: x[1])
        min_heap = []

        cur = 0
        for num, frm, to in trips:
            while min_heap and min_heap[0][0] <= frm:
                cur -= heapq.heappop(min_heap)[1]
            cur += num
            if cur > capacity:
                return False
            heapq.heappush(min_heap, [to, num])
        
        return True