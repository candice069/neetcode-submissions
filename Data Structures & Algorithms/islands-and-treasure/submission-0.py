class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        dirs = [
            (0,1), (0,-1), (1,0), (-1, 0)
        ]
        queue = deque()
        m, n = len(grid), len(grid[0])

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    queue.append((r,c))
        
        while queue:
            r, c = queue.popleft()

            for dr, dc in dirs:
                nr, nc = r+dr, c+dc
                if nr < 0 or nc < 0 or nr >=m or nc >= n:
                    continue
                if grid[nr][nc] !=2147483647 :
                    continue
                
                if grid[nr][nc] == 2147483647:
                    grid[nr][nc] = grid[r][c] + 1
                    queue.append((nr, nc))