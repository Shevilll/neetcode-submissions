class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        if not prerequisites:
            return [False] * len(queries)
        def dfs(i, src):
            if i in seen:
                return
            seen.add(i)
            
            if i != src:
                visit[src].add(i)


            for nei in adj[i]:
                dfs(nei, src)


        adj = {i:[] for i in range(numCourses)}

        for u, v in prerequisites:
            adj[u].append(v)

        visit = defaultdict(set)

        for i in range(numCourses):
            seen = set()
            dfs(i, i)

        ans = []

        for u, v in queries:
            if v in visit[u]:
                ans.append(True)
            else:
                ans.append(False)
        return ans