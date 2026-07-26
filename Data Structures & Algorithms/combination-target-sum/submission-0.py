class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(start, s, path):
            if s == target:
                res.append(path[:])
                return
            
            if s > target:
                return
            
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i, s + nums[i], path)
                path.pop()
        backtrack(0,0,[])
        return res