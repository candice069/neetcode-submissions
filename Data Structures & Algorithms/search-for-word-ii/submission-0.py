class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Solution:
    def __init__(self):
        self.root = TrieNode()

    def findWords(
        self,
        board: List[List[str]],
        words: List[str]
    ) -> List[str]:

        # 1. Build Trie from words
        for word in words:
            node = self.root

            for c in word:
                if c not in node.children:
                    node.children[c] = TrieNode()

                node = node.children[c]

            # Store the complete word at its ending node
            node.word = word

        rows = len(board)
        cols = len(board[0])
        directions = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0)
        ]

        visited = [
            [False for _ in range(cols)]
            for _ in range(rows)
        ]

        res = []

        def dfs(i, j, node):
            # Boundary check
            if i < 0 or i >= rows or j < 0 or j >= cols:
                return

            # Cannot reuse the same board position
            if visited[i][j]:
                return

            c = board[i][j]

            # Current path does not exist in Trie
            if c not in node.children:
                return

            # Move to the Trie node for the current character
            next_node = node.children[c]

            # Found a complete word
            if next_node.word is not None:
                res.append(next_node.word)

                # Avoid adding the same word multiple times
                next_node.word = None

            visited[i][j] = True

            for di, dj in directions:
                dfs(i + di, j + dj, next_node)

            # Backtracking
            visited[i][j] = False

        # 3. Every cell can be the starting position
        for i in range(rows):
            for j in range(cols):
                dfs(i, j, self.root)

        return res