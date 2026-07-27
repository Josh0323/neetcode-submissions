class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_ind = {}

        for i, c in enumerate(s):
            last_ind[c] = i
        
        result = []
        start_ind = 0
        part_end = -1
        for i, c in enumerate(s):
            if last_ind[c] > part_end:
                part_end = last_ind[c]
            
            if part_end == i:
                result.append(i - start_ind + 1)
                start_ind = i + 1

        return result