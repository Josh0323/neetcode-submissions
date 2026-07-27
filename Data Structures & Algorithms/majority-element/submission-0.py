class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = defaultdict(int)
        threshold = len(nums) // 2
        for n in nums:
            hashmap[n] += 1
            if hashmap[n] > threshold:
                return n
        