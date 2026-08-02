class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def splitable(top):
            subarr, cur = 1, 0

            for n in nums:
                cur += n
                if cur > top:
                    subarr += 1
                    if subarr > k:
                        return False
                    cur = n
            return True
        
        l, r = max(nums), sum(nums)
        while l < r:
            m = l + (r - l) // 2
            if splitable(m):
                r = m
            else:
                l = m + 1
        
        return l