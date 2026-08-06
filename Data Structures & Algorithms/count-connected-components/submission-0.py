class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjs = defaultdict(list)
        for a, b in edges:
            adjs[a].append(b)
            adjs[b].append(a)
        
        visited = set()
        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)
            for adj in adjs[node]:
                if adj not in visited:
                    dfs(adj)
        
        cnt = 0
        for i in range(n):
            if i not in visited:
                cnt += 1
                dfs(i)
        return cnt

        