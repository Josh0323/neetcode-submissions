class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)
        
        for n in nums:
            count[n] += 1

            if len(count) <= 2:
                continue
            
            n_count = defaultdict(int)
            for k, v in count.items():
                if v > 1:
                    n_count[k] = v - 1
            count = n_count

        return [k for k in count if nums.count(k) > len(nums) // 3]
            
