class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()

        ran = [-1] * max([i for _, i in intervals])
        for l, r in intervals:
            cur_len = r - l + 1
            i = l - 1
            while i < r:
                ran[i] = cur_len if ran[i] == -1 else min(ran[i], cur_len)
                i += 1

        result = []

        for q in queries:
            result.append(-1 if q > len(ran) else ran[q - 1])
            
        
        return result