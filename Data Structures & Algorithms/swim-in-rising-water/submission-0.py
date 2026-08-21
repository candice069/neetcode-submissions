class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        #using kruskal's algorithm
        dirs = [
            (0,1), (1,0)
        ]
        n = len(grid)
        edges = []
        for r in range(n):
            for c in range(n):
                node = r * n + c

                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    nei = nr *n + nc
                    if nr < n and nc <n:
                        weight = max(grid[r][c], grid[nr][nc])
                        edges.append((weight, node, nei))
        edges.sort()
        parent = [i for i in range(n*n)]
        rank = [1] * (n*n)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            r1 = find(x)
            r2 = find(y)
            if r1 == r2:
                return False
            
            if rank[r1] < rank[r2]:
                parent[r1] = r2
            elif rank[r1] > rank[r2]:
                parent[r2] = r1
            else:
                parent[r2] = r1
                rank[r1] += 1
        
        for weight, node, nei in edges:
            union(node, nei)

            if find(0) == find(n*n-1):
                return weight
        return 0