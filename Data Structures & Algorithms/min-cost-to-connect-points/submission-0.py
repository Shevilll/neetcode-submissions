class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = defaultdict(list)

        for i in range(len(points)):
            for j in range(i, len(points)):
                xi, yi = points[i][0], points[i][1]
                xj, yj = points[j][0], points[j][1]

                cost = abs(xi - xj) + abs(yi - yj)

                adj[(xi, yi)].append(((xj, yj), cost))
                adj[(xj, yj)].append(((xi, yi), cost))

        visit = set()

        pq = [(0, (0, 0))]

        ans = 0

        while pq:
            cost, curr = heapq.heappop(pq)

            if curr in visit:
                continue

            visit.add(curr)
            ans += cost

            for next, new_cost in adj[curr]:
                if next not in visit:
                    heapq.heappush(pq, (new_cost, next))

        
        return ans