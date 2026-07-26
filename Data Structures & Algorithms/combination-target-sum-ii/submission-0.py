class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtrack(start, s, path):
            if s == target:
                res.append(path[:])
                return 
            if s > target:
                return
            
            for i in range(start, len(candidates)):
                x = candidates[i]
                if i >start and x == candidates[i - 1]:
                    continue
                path.append(x)
                backtrack(i + 1, s + x, path)
                path.pop()
        backtrack(0, 0, [])
        return res
