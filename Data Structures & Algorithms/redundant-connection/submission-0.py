class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #there is only path between a and b, so we just need to check this
        adjs = defaultdict(list)
        
        def dfs(i, target, visited):
            if i == target:
                return True
            visited.add(i)
            
            for adj in adjs[i]:
                if adj not in visited:
                    if dfs(adj, target, visited):
                        return True
            return False
        
        for a, b in edges:
            visited = set()
            
            if dfs(a, b , visited):
                return [a,b]
            
            adjs[a].append(b)
            adjs[b].append(a)