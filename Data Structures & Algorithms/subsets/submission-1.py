class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]

        for n in nums:
            cur_len = len(result)
            for i in range(cur_len):
                new_item = result[i] + [n]
                result.append(new_item)
        
        return result

