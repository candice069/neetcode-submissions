class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #connected + no cycle
        if len(edges) != n-1:
            return False
        
        visited = [False for _ in range(n)]
        adjs = defaultdict(list)
        for a, b in edges:
            adjs[a].append(b)
            adjs[b].append(a)

        def dfs(i):
            visited[i] = True
            
            for adj in adjs[i]:
                if visited[adj] == False:
                    dfs(adj)
        dfs(0)
        if False in visited:
            return False
        return True
        