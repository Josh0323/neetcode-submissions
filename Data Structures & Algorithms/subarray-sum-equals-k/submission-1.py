class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count, current_prefix_sum = 0, 0
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1

        for n in nums:
            current_prefix_sum += n
            needed_prefix_sum = current_prefix_sum - k
            count += prefix_sum[needed_prefix_sum]
            prefix_sum[current_prefix_sum] += 1
        
        return count