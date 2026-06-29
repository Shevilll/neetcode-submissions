class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        def dfs(i):
            if i in visit:
                return
            
            visit.add(i)

            for nei in adj[i]:
                dfs(i)

            top.append(i)


        adj = {i:[] for i in range(numCourses)}

        for u, v in prerequisites:
            adj[u].append(v)

        visit = set()
        top = []

        for i in range(numCourses):
            dfs(i)

        ans = []

        for u, v in queries:
            if v in top[top.index(u):]:
                ans.append(False)
            else:
                ans.append(True)
        return ans