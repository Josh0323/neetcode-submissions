class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        kl, ku = 1, max(piles)

        result = 0
        while kl <= ku:
            k = kl + (ku - kl) // 2
            total_time = 0
            for p in piles:
                total_time += math.ceil(p / k)
            
            if total_time > h:
                kl = k + 1
            elif total_time <= h:
                result = k
                ku = k - 1
        
        return result

