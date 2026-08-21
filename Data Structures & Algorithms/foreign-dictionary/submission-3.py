class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = defaultdict(set)
        for word in words:
            for char in word:
                adj[char] = set()
        
        n = len(words)
        for i in range(0, n-1):
            a, b = words[i], words[i+1]
            if len(a) > len(b) and a.startswith(b):
                return ""
            for j in range(min(len(a), len(b))):
                if a[j] != b[j]:
                    adj[a[j]].add(b[j])
                    break
        
        state = {}
        stack = []
        def dfs(node):
            if state.get(node, 0) == 1:
                return False
            if state.get(node, 0) == 2:
                return True
            state[node] = 1
            for nei in adj[node]:
                if not dfs(nei):
                    return False
            state[node] = 2
            stack.append(node)
            return True
        for char in adj:
            # if state.get(char, 0) == 0:
            if not dfs(char):
                return ""
        ans = ""
        while stack:
            ans += str(stack.pop())
        return ans