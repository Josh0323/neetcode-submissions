class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
    
    def add_word(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.is_end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        R, C = len(board), len(board[0])
        root = TrieNode()

        for w in words:
            root.add_word(w)

        result, visited = set(), set()
        def backtrack(r, c, node, word):
            if not 0 <= r < R or not 0 <= c < C or board[r][c] not in node.children or (r, c) in visited:
                return

            
            
            visited.add((r, c))
            word += board[r][c]
            node = node.children[board[r][c]]

            if node.is_end:
                result.add(word)

            backtrack(r + 1, c, node, word)
            backtrack(r - 1, c, node, word)
            backtrack(r, c + 1, node, word)
            backtrack(r, c - 1, node, word)
            visited.remove((r, c))



        
        for r in range(R):
            for c in range(C):
                backtrack(r, c, root, "")
        
        return list(result)