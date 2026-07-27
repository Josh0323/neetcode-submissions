class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = set()

        for t in triplets:
            if any(i > j for i, j in zip(t, target)):
                continue
            
            for i, v in enumerate(t):
                if v == target[i]:
                    good.add(i)
        
        return len(good) == 3