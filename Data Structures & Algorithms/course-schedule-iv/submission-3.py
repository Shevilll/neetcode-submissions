class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        def dfs(i, src):
            if i in visit:
                return
            
            if i != src:
                visit[src].add(i)

            for nei in adj[i]:
                dfs(nei, src)


        adj = {i:[] for i in range(numCourses)}

        for u, v in prerequisites:
            adj[u].append(v)

        visit = defaultdict(set)

        for i in range(numCourses):
            dfs(i, i)

        ans = []
        print(visit)
        for u, v in queries:
            if u in visit[v]:
                ans.append(False)
            else:
                ans.append(True)
        return ans