class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dirs = [
            (0,1), (0,-1), (1,0), (-1,0)
        ]
        cnt = 0
        max_cnt = 0

        m = len(grid)
        n = len(grid[0])

        def dfs(r, c):
            nonlocal cnt
            if r < 0 or c <0 or r >= m or c >=n:
                return
            if grid[r][c] != 1:
                return
            grid[r][c] = 0
            cnt += 1

            for dr, dc in dirs:
                dfs(r + dr, c + dc)
        for i in range(m):
            for j in range(n):
                cnt = 0
                dfs(i, j)
                max_cnt = max(max_cnt, cnt)
        return max_cnt