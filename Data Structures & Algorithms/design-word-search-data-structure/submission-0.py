class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        node = self.root

        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.end = True   
        

    def search(self, word: str) -> bool:
        #since it has '.' which can represent any char in the string, so if we meet it, should look all ways
        def dfs(node, index):
            if index == len(word):
                return node.end

            c = word[index]
            if c != '.':
                if c not in node.children:
                    return False
                return dfs(node.children[c], index+1)   

            else:
                #c=='.' 
                for children in node.children.values():
                    if dfs(children,index+1):
                        return True
                return False
        return dfs(self.root, 0)
