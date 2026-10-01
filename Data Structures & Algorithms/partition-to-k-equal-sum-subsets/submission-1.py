class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0:
            return False
        
        sub_sum = sum(nums) // k

        subs = [0] * k

        nums.sort(reverse=True)
        def dfs(i):
            if i == len(nums):
                return True
            for side in range(k):
                if subs[side] + nums[i] <= sub_sum:
                    subs[side] += nums[i]
                    if dfs(i + 1):
                        return True
                    subs[side] -= nums[i]

                if subs[side] == 0:
                    break
            return False
        return dfs(0)