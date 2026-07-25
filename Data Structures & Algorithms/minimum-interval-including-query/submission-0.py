class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key = lambda x: x[0])
        res = [-1] *len(queries)

        #sort queries also
        sorted_queries = sorted((query, i) for i, query in enumerate(queries))

        heap = []
        j = 0#iterate from the first interval
        for query, i in sorted_queries:
            #store each interval to heap, each time 'start' should less than query
            #since we have sorted query and intervals, so the time is from left to right
            while j < len(intervals) and intervals[j][0] <= query:
                start, end = intervals[j][0], intervals[j][1]
                size = end - start +1
                heapq.heappush(heap, (size, end))
                j+=1
            
            #if some intervals have ended in heap, just pop them
            while heap and heap[0][1] < query:
                heapq.heappop(heap)
            if heap:
                res[i] = heap[0][0]
        return res
            