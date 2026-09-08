class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        #unordered
        result= []
        def backtracking(path, start):
            if len(path) == k:
                result.append(path[:])
                return
            for i in range(start, n+1):
                path.append(i)
                backtracking(path, i+1)
                path.pop()
        backtracking([], 1)
        return result