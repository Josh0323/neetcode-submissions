class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i, j = 0, 0
        seen = set()
        while i - j <= k and i < len(nums):
            if nums[i] in seen:
                return True
            seen.add(nums[i])
            i += 1
        
        while i < len(nums):
            seen.remove(nums[j])
            if nums[i] in seen:
                return True
            seen.add(nums[i])
            
            i, j = i + 1, j + 1
        
        return False
        