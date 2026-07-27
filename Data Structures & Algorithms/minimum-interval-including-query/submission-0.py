class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()

        result = []

        for q in queries:
            cur_len = 1e5
            for l, r in intervals:
                if l <= q <= r:
                    cur_len = min(r - l + 1, cur_len)
            result.append(cur_len if cur_len != 1e5 else -1)
        
        return result