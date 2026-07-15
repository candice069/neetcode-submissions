class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.end = True


    def search(self, word: str) -> bool:
        node = self.root

        for w in word:
            if w not in node.children:
                return False
            node = node.children[w]
        return node.end == True
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root

        for p in prefix:
            if p not in node.children:
                return False
            node = node.children[p]
        return True
        
        