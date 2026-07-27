class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val = prices[0]
        profit = 0
        for p in prices:
            diff = p - min_val

            if diff > 0:
                profit += diff
            min_val = p
            
        return profit