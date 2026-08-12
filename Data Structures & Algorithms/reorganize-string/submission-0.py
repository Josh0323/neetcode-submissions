class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        max_heap = [[count, char] for char, count in count.items()]
        heapq.heapify_max(max_heap)

        prev, res = None, ""

        while max_heap or prev:
            if prev and not max_heap:
                return ""
            
            count, char = heapq.heappop_max(max_heap)
            res += char
            count -= 1

            if prev:
                heapq.heappush_max(max_heap, prev)
                prev = None
            
            if count != 0:
                prev = [count, char]
            
        return res