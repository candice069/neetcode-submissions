class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]

        m = len(grid)
        n = len(grid[0])

        def dfs(r, c):
            if r <0 or c < 0 or r >=m or c >= n:
                return
            if grid[r][c] != '1':
                return
            
            grid[r][c] = '0' #make the visited node become '0'

            for dr, dc in dirs:
                dfs(r+dr, c+dc)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    cnt += 1
                    dfs(i, j)
        return cnt