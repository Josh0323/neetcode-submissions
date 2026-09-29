class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if sum(matchsticks) % 4 != 0:
            return False
        side = sum(matchsticks) / 4
        matchsticks.sort(reverse=True)
        result = [0] * 4
        def dfs(i):
            if all(item == side for item in result):
                return True

            for j in range(4):
                if result[j] + matchsticks[i] <= side:
                    result[j] += matchsticks[i]
                    if dfs(i + 1):
                        return True
                    result[j] -= matchsticks[i]
            return False
        return dfs(0)