class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        def dfs(i):
            if i in path:
                return False
            if i in visit:
                return True

            visit.add(i)
            path.add(i)
            k = True
            
            for nei in adj[i]:
                k = dfs(nei)

            path.remove(i)
            res.append(i)
            return k

        adj = {i:[] for i in range(n)}

        for u, v in edges:
            adj[u].append(v)
        print(adj)
        path = set()
        visit = set()

        res = []

        for i in range(n):
            if not dfs(i):
                return []
        
        res.reverse()

        return res

        