from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = []
        time = 0

        cnt = Counter(tasks)
        for task, freq in cnt.items():
            heapq.heappush(heap, (-freq, task))
        
        cooldown = deque()

        while heap or cooldown:
            time += 1
            while cooldown and cooldown[0][2] <= time:
                freq, task, avail_time = cooldown.popleft()
                heapq.heappush(heap, (freq, task))
            if heap:
                x = heapq.heappop(heap)
                task = x[1]
                freq = x[0] + 1
                if freq != 0:
                    cooldown.append((freq, task, time+n+1))
        return time
            
                
