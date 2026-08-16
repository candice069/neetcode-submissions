class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjs = defaultdict(list)
        #record each node's target node as {node : (target, time)}
        for node, target, time in times:
            adjs[node].append((target, time))

        #we need the minimum of the node that takes the longest time to get
        #use heap to handle least got time first
        total_time = 0
        heap = [(0, k)] #represent the time from k
        visited = set()

        while heap:
            current_time, node = heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            total_time = current_time

            for target, time in adjs[node]:
                if target not in visited:
                    heapq.heappush(heap, (current_time + time, target))
            
        if len(visited) != n:
            return -1
        return total_time
        
        