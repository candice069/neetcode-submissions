class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if len(points) <= k :
            return points
        heap = []
        res = []

        for i in range(len(points)):
            distance = points[i][0]**2 + points[i][1]**2
            heapq.heappush(heap, (-distance, i))
        
        while len(heap) > k:
            heapq.heappop(heap)
        
        while heap:
            x = heapq.heappop(heap)
            res.append(points[x[1]])
        return res