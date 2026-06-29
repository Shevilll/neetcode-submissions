class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(i):
            if i in path:
                return False
            if i in visit:
                return True

            path.add(i)
            visit.add(i)
            k = True
            for nei in adj[i]:
                k = dfs(nei)

            path.remove(i)
            return k

        
        adj = {i:[] for i in range(numCourses)}

        for u, v in prerequisites:
            adj[u].append(v)

        path = set()
        visit = set()

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True