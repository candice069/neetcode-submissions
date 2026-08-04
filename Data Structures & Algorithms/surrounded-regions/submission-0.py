class Solution:
    def solve(self, board: List[List[str]]) -> None:
        dirs = [
            (0,1), (0,-1), (1,0), (-1,0)
        ]
        m, n = len(board), len(board[0])

        queue = deque()
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and (i == 0 or j == 0 or i == m-1 or j == n - 1):
                    queue.append((i, j))
                    board[i][j] = 'B'
        
        while queue:
            r, c = queue.popleft()

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if nr < 0 or nc < 0 or nr > m-1 or nc > n-1:
                    continue
                if board[nr][nc] != 'O':
                    continue
                
                board[nr][nc] = 'B'
                queue.append((nr, nc))
        for r in range(m):
            for c in range(n):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'B':
                    board[r][c] = 'O'



        