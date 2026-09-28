class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        count = Counter(nums)

        def dfs(cur):
            if len(cur) == len(nums):
                result.append(cur.copy())
                return
            
            for num in count:
                if count[num] > 0:
                    cur.append(num)
                    count[num] -= 1
                    dfs(cur)

                    count[num] += 1
                    cur.pop()
            
        dfs([])
        return result