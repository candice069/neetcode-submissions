class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for start, dest, price in flights:
            adj[start].append((price, dest))
        
        heap = [(0, src, 0)]#(cost, start, flight_cnt)
        best = [[float('inf')]* (k+2) for _ in range(n)]
        best[src][0] = 0
        while heap:
            cost, start, flight_cnt = heapq.heappop(heap)
            if start == dst:
                return cost
            if flight_cnt == k+1:
                continue
            for price, nei in adj[start]:
                new_cost = price+ cost
                new_flight= flight_cnt + 1

                if new_cost < best[nei][new_flight]:
                    best[nei][new_flight] = new_cost
                    heapq.heappush(heap, (cost+price, nei, flight_cnt + 1))
        return -1