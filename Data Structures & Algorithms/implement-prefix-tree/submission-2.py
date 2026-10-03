class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root

        for c in word:
            i = ord(c) - ord("a")
            if cur.children[i] == None:
                
                cur.children[i] = TrieNode()
            cur = cur.children[i]
        cur.is_end = True

    def search(self, word: str) -> bool:
        cur = self.root

        for c in word:
            i = ord(c) - ord("a")
            if cur.children[i] == None:
                return False
            cur = cur.children[i]
        return cur.is_end        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for c in prefix:
            i = ord(c) - ord('a')
            if cur.children[i] == None:
                return False
            cur = cur.children[i]
        
        return True
        