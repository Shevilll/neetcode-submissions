class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def dfs(i):
            if i in path:
                return False

            if i in visit:
                return True

            visit.add(i)
            path.add(i)

            for nei in adj[i]:
                if nei in path:
                    return False
                dfs(nei)
            
            path.remove(i)
            top.append(i)
            return True

        adj = {i:[] for i in range(numCourses)}

        for u, v in prerequisites:
            adj[u].append(v)

        visit = set()
        path = set()
        top = []

        for i in range(numCourses):
            if not dfs(i):
                return []
        

        for i in range(numCourses):
            if i not in visit:
                top.append(i)

        return top
