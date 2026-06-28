class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = {i:[] for i in range(n)}

        for s, e, w in edges:
            adj[s].append((e, w))

        
        res = {}

        minHeap = [(0, src)]

        while minHeap:
            w, s = heapq.heappop(minHeap)

            if s in res:
                continue

            res[s] = w

            for ee, ew in adj[s]:
                if ee in res:
                    continue
                heapq.heappush(minHeap, (w + ew, ee))

        for i in range(n):
            if i not in res:
                res[i] = -1

        return res