import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for s in stones:
            heapq.heappush(heap, -s)
        
        while len(heap) >= 2:
            x = -heapq.heappop(heap)
            y = -heapq.heappop(heap)

            if x == y:
                continue
            else:
                heapq.heappush(heap, -abs(y-x))
        if not heap:
            return 0
        else:
            return -heap[0]
