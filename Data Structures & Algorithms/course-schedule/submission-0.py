class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {}

        for i, j in prerequisites:
            if i not in adj:
                adj[i] = []
            if j not in adj:
                adj[j] = []
            adj[i].append(j)

        visit = set()
        complete = set()

        def dfs(node):
            if node in complete:
                return True
            if node in visit:
                return False
            
            visit.add(node)
            if node in adj:
                for i in adj[node]:
                    if not dfs(i):
                        return False
            visit.remove(node)
            complete.add(node)
            return True

        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True