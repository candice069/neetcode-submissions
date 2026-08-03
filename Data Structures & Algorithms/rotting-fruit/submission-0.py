class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minutes = 0
        dirs = [
            (0,1), (0,-1), (1,0), (-1,0)
        ]
        m, n = len(grid), len(grid[0])

        queue = deque()
        fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        
        while queue and fresh > 0:
            level_size = len(queue)
            for _ in range(level_size):
                r, c  = queue.popleft()

                for dr, dc in dirs:
                    nr, nc = r+dr, c + dc

                    if nr < 0 or nc < 0 or nr >= m or nc >= n:
                        continue
                    if grid[nr][nc] !=1:
                        continue
                    
                    grid[nr][nc] = 2
                    fresh -= 1
                    queue.append((nr, nc))
            minutes += 1
        if fresh != 0:
            return -1
        return minutes

             