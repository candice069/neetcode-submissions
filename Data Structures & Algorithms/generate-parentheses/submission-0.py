class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(path, left_cnt, right_cnt):
            if len(path) == 2 * n:
                res.append("".join(path))
            if left_cnt < n:
                path.append('(')
                backtrack(path, left_cnt+1, right_cnt)
                path.pop()
            
            if left_cnt > right_cnt:
                path.append(')')
                backtrack(path, left_cnt, right_cnt+1)
                path.pop()
        backtrack([], 0, 0)
        return res