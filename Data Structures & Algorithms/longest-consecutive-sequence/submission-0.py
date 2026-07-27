class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniq_nums = set(nums)
        longest_seq = 0

        for n in uniq_nums:
            if n - 1 in uniq_nums:
                continue
            i = 1
            while True:
                if n + i in uniq_nums:
                    i += 1
                else:
                    longest_seq = max(longest_seq, i)
                    break
        
        return longest_seq