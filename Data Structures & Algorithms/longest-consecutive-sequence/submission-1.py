class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniq_nums = set(nums)
        longest_seq = 0

        for n in uniq_nums:
            if n - 1 in uniq_nums:
                continue
            length = 1
            while n + length in uniq_nums:
                length += 1
            
            longest_seq = max(longest_seq, length)
        
        return longest_seq