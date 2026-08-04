class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        learn = set() #record the coures that have been token
        record = defaultdict(list)

        for course, pre in prerequisites:
            record[course].append(pre)
        
        def dfs(course):
            if not record[course]:
                return True
            #detect if there are any cycles
            if course in learn:
                return False
            learn.add(course)
            
            for p in record[course]:
                if not dfs(p):
                    return False
            
            learn.remove(course)
            record[course] = [] #mark as token
            return True
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True