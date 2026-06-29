class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)

        minHeap = [(grid[0][0], 0, 0)]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        visit = set((0, 0))
        
        while minHeap:
            ti, ui, vi = heapq.heappop(minHeap)

            if ui == N - 1 and vi == N - 1:
                return ti


            for x, y in directions:
                nu, nv = ui + x, vi + y

                if (nu, nv) in visit or nu < 0 or nv < 0 or nu == N or nv == N:
                    continue
                visit.add((nu, nv))
                heapq.heappush(minHeap, (max(ti, grid[nu][nv]), nu, nv))

            