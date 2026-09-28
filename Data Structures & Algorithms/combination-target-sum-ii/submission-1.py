class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        def dfs(i, comb, cur_sum):
            if cur_sum == target:
                result.append(comb.copy())
                return
            
            if i == len(candidates) or cur_sum > target:
                return
            
            comb.append(candidates[i])
            dfs(i + 1, comb, cur_sum + candidates[i])
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            comb.pop()
            dfs(i + 1, comb, cur_sum)
        
        dfs(0, [], 0)
        return result
