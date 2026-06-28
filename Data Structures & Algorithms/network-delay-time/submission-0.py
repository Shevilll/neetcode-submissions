class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i:[] for i in range(1, n + 1)}

        for ui, vi, ti in times:
            adj[ui].append((vi, ti))

        shortest = {}

        minHeap = [(0, k)]

        while minHeap:
            ti, ui = heapq.heappop(minHeap)

            if ui in shortest:
                continue

            shortest[ui] = ti

            for vi, vti in adj[ui]:
                if vi not in shortest:
                    heapq.heappush(minHeap, (vti + ti, vi))

        for i in range(1, n + 1):
            if i not in shortest:
                return -1

        return max(shortest.values())