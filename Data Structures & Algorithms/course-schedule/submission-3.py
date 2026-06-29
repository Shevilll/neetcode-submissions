class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(i):
            if i in path:
                return False
            if i in visit:
                return True

            path.add(i)
            visit.add(i)

            for nei in adj[i]:
                if nei in path:
                    return False
                dfs(nei)

            path.remove(i)
            return True

        
        adj = {i:[] for i in range(numCourses)}

        for u, v in prerequisites:
            adj[u].append(v)

        path = set()
        visit = set()

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True