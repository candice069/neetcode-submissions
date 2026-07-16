class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None
class Solution:
    def __init__(self):
        self.root = TrieNode()
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        #store words in trie
        for word in words:
            node = self.root
            for c in word:
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]
            node.word = word
        
        m = len(board)
        n = len(board[0])
        directions = [(0,1), (0,-1), (-1,0), (1,0)]#right, left, up, down
        visited = [[False for _ in range(n)] for _ in range(m)]
        res = []
        
        def dfs(i, j, node):
            if i < 0 or i>= m or j< 0 or j >=n:
                return 
            if visited[i][j]:
                return 
            c = board[i][j]
            if c not in node.children:
                return
            
            nxt_node = node.children[c]#else, it has children[c]
            if nxt_node.word is not None:
                res.append(nxt_node.word) 

                nxt_node.word = None
            
            visited[i][j] =True
            for di, dj in directions:
                dfs(i+di, j+dj, nxt_node)
            visited[i][j] = False
        
        for i in range(m):
            for j in range(n):
                dfs(i, j, self.root)
        return res
            
        