class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        count = [a, b, c]
        result = []

        def get_max(repeated):
            idx = -1
            max_count = 0
            for i in range(3):
                if i == repeated or count[i] == 0:
                    continue
                if max_count < count[i]:
                    max_count = count[i]
                    idx = i
            return idx
        
        repeated = -1
        while True:
            max_char = get_max(repeated)
            if max_char == -1:
                break
            result.append(chr(max_char + ord('a')))
            count[max_char] -= 1

            if len(result) > 1 and result[-1] == result[-2]:
                repeated = max_char
            else:
                repeated = -1

        return ''.join(result)    