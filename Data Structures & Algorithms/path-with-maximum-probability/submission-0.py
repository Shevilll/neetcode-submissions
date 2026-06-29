class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = defaultdict(list)

        for i in range(len(edges)):
            src, dst = edges[i]
            adj[src].append((dst, succProb[i]))
            adj[dst].append((src, succProb[i]))

        pq = [(-1, start_node)]

        visit = set()

        while pq:
            prob, curr = heapq.heappop(pq)
            visit.add(curr)
            if curr == end_node:
                return -prob
            
            for dst, pr in adj[curr]:
                if dst not in visit:
                    heapq.heappush(pq, (prob * pr, dst))
            
        
        return 0.0