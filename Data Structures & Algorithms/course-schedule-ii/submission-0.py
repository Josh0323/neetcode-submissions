class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereqs = {cls : [] for cls in range(numCourses)}

        for cls, pre in prerequisites:
            prereqs[cls].append(pre)
        
        results = []
        visited, circle = set(), set()

        def dfs(cls):
            if cls in circle:
                return False
            
            if cls in visited:
                return True
            
            circle.add(cls)
            for pre in prereqs[cls]:
                if not dfs(pre):
                    return False
            circle.remove(cls)

            visited.add(cls)
            results.append(cls)
            return True
        
        for cls in range(numCourses):
            if not dfs(cls):
                return []
        
        return results