class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        #using kruskal's algorithm
        heap = []
        n =len(points)
        for i, x in enumerate(points):
            if i < len(points) - 1:
                for j in range(i+1, len(points)):
                    y = points[j]
                    distance = abs(x[0] - y[0]) + abs(x[1] - y[1])
                    heapq.heappush(heap, (distance, i, j))
        
        parent = [i for i in range(n)]
        rank = [1] * n
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            root1 = find(x)
            root2 = find(y)   
            if root1 == root2:
                return False
            if rank[root1] > rank[root2]:
                parent[root2] = root1
            elif rank[root2] > rank[root1]:
                parent[root1] = root2
            else:
                parent[root2] = root1
                rank[root1] += 1
            return True
        cnt_edge = 0
        ans = 0
        while heap and cnt_edge < n - 1:
            distance, i, j = heapq.heappop(heap)
            if union(i, j):
                cnt_edge += 1
                ans += distance
        return ans

        