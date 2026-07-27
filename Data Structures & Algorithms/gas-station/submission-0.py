class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        ind = -1

        def dfs(i, g, p):
            if p == len(gas):
                return 0
            i = i % len(gas)
            if gas[i] + g >= cost[i]:
                return 1 + dfs(i + 1, gas[i] + g - cost[i], 1 + p)
            else:
                return float('-inf')

        for i in range(len(gas)):
            path = dfs(i, 0, 0)
            if path == len(gas):
                return i
 
        return ind