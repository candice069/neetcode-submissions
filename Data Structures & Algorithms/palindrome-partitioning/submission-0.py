class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def if_palindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        def backtrack(start, path):
            if start == len(s):
                res.append(path[:])
                return
            
            for i in range(start, len(s)):
                if not if_palindrome(start, i):
                    continue
                path.append(s[start:i+1])
                backtrack(i+1, path)
                path.pop()
        backtrack(0, [])
        return res