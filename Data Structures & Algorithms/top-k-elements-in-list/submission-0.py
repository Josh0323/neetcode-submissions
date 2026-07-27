class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        ns = Counter(nums)
        result = {k: v for k, v in sorted(ns.items(), key = lambda item:item[1], reverse=True)}
        return list(result.keys())[:k]