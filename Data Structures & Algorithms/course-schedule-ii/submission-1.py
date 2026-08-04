class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ans = []
        learning = set()
        token = set()
        record = defaultdict(list)

        for course, pre in prerequisites:
            record[course].append(pre)
        
        def dfs(course):
            if course in token:
                return True
            if course in learning:
                return False

            learning.add(course)
            for pre in record[course]:
                if not dfs(pre):
                    return False
            token.add(course)
            ans.append(course)
            return True
        for course in range(numCourses):
            if not dfs(course):
                return []
        return ans
            
            
        