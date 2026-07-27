class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ''

        for s in strs:
            result += str(len(s)) + '#' + s
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            start = i
            while s[i] != '#':
                i += 1
            token_len = int(s[start:i])
            i += 1
            retrieved_token = s[i: i + token_len]
            result.append(retrieved_token)
            i += token_len
        return result