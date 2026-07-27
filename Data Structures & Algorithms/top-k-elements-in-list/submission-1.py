class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        count = Counter(nums)

        freq = [[] for _ in range(len(nums) + 1)]

        for key, c in count.items():
            freq[c].append(key)
        
        result  = []
        for l in reversed(freq):
            for i in l:
                result.append(i)
                if len(result) == k:
                    return result