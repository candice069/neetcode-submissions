class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjs = defaultdict(list)
        neighbours = defaultdict(list)
        #adjs:{node:[(target1, time1),(target2, time2)]}
        for i in range(len(times)):
            node = times[i][0]
            target = times[i][1]
            time = times[i][2]
            adjs[node].append((target,time))
            neighbours[node].append(target)

        #use heap, we need to find the minimum of the maximum gotten node
        heap = [(0, k)]
        total_time = 0
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