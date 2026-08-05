class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)

        for i, v in edges:
            adj[i].append(v) 
            adj[v].append(i) 


        visit = set()

        def dfs(i, par):
            if i in visit:
                return False

            visit.add(i)

            for nei in adj[i]:
                if nei == par:
                    continue
                if not dfs(nei, i):
                    return False

            return True

        return dfs(0, -1) and n == len(visit)