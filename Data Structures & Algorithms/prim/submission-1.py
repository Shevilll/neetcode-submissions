class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)

        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        visit = set()

        ans = 0

        pq = [(0, 0)]

        while pq:
            w, u = heapq.heappop(pq)

            if u in visit:
                continue

            visit.add(u)
            ans += w

            for newu, neww in adj[u]:
                heapq.heappush(pq, (neww, newu))

        if len(visit) != n:
            return -1
        return ans