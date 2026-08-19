class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adjs= defaultdict(list)
        for source, destination in tickets:
            adjs[source].append(destination)
        
        for source in adjs:
            adjs[source].sort(reverse = True)
        
        ans = []
        
        def dfs(airport):
            while adjs[airport]:
                nxt = adjs[airport].pop()
                dfs(nxt)
            ans.append(airport)
        
        dfs("JFK")
        return ans[::-1]
