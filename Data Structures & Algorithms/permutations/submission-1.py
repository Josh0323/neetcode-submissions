# review
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perm = [[]]

        for num in nums:
            new_perm = []
            for p in perm:
                for i in range(len(p) + 1):
                    p_copy = p.copy()
                    p_copy.insert(i, num)
                    new_perm.append(p_copy)
            perm = new_perm
        return perm
