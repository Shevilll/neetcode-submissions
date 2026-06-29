class UnionFind:
    def __init__(self, n):
        self.par = {}
        self.rank = {}
        for i in range(n):
            self.par[i] = i
            self.rank[i] = 0

    def union(self, x, y):
        x1, y1 = self.find(x), self.find(y)

        if x1 == y1:
            return False

        if self.rank[x1] > self.rank[y1]:
            self.par[x1] = y1
        elif self.rank[y1] > self.rank[x1]:
            self.par[y1] = x1
        else:
            self.par[x1] = y1
            self.rank[x1] += 1
        
        return True

    def find(self, x):
        n = self.par[x]

        while n != self.par[n]:
            self.par[n] = self.par[self.par[n]]
            n = self.par[n]

        return n

class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        pq = []

        for u, v, w in edges:
            heapq.heappush(pq, (w, u, v))

        res = 0
        k = 0
        uf = UnionFind(n)
        while k < n - 1 and pq:
            w, u, v = heapq.heappop(pq)

            if not uf.union(u, v):
                continue
            k += 1
            res += w
        
        if k != n - 1:
            return -1
        return res