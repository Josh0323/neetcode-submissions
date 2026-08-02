class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def calc_days(cap):
            d, cur = 0, 0 
            for w in weights:
                if cur + w > cap:
                    d += 1
                    cur = w
                else:
                    cur += w
            return d + 1
        
        l, r = max(weights), sum(weights)

        while l < r:
            m = l + (r - l) // 2
            if calc_days(m) > days:
                l = m + 1
            else:
                r = m
        return l