class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)

        stack = []

        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                last_t, last_i = stack.pop()
                result[last_i] = i - last_i
            stack.append((t, i))

        return result