class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_ind = {}

        for i, c in enumerate(s):
            last_ind[c] = i
        
        result = []
        size, end = 0, 0
        for i, c in enumerate(s):
            size += 1
            end = max(end, last_ind[c])
            
            if end == i:
                result.append(size)
                size = 0

        return result