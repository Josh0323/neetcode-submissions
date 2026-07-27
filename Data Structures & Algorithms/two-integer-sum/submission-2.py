class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = defaultdict(int)

        for i, v in enumerate(nums):
            if v in hashmap:
                return [hashmap[v], i]
            key = target - v
            hashmap[key] = i
