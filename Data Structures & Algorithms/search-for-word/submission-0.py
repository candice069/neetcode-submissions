class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        m = len(board)
        n = len(board[0])
        visited = [[False] * n for _ in range(m)]

        def dfs(i, j, index):
            if i < 0 or j < 0 or i >= m or j >= n or visited[i][j] == True or board[i][j] != word[index]:
                return False
            if index == len(word)-1:
                return True
            
            visited[i][j] = True
            for r, c in directions:
                if dfs(i+r, j+c, index+1):
                    return True
            visited[i][j] = False
            return False
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False
           
        