class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        dirs = [
            (0,1), (0,-1), (1,0), (-1,0)
        ] 
        #use dfs to get which grid can get Pacific or Atlantic
        P, A = set(), set()
        m, n = len(heights), len(heights[0])

        def dfs(r, c, visited):
            visited.add((r,c))

            for dr, dc in dirs:
                nr, nc = r+dr, c + dc
                if nr < 0 or nc <0 or nr >= m or nc >= n:
                    continue
                if (nr, nc) in visited:
                    continue
                if heights[nr][nc] < heights[r][c]:
                    continue
                dfs(nr, nc, visited)
        
        
        for c in range(n):
            dfs(0, c, P)
        for r in range(m):
            dfs(r, 0, P)
        
        for c in range(n):
            dfs(m-1, c, A)
        for r in range(m):
            dfs(r, n-1, A)
        
        for r in range(m):
            for c in range(n):
                if (r,c) in P and (r,c) in A:
                    res.append([r,c])
        return res