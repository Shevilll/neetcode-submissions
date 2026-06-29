class UnionFind:
    def __init__(self, n):
        self.par = {}
        self.rank = {}

        for i in range(n):
            self.par[i] = i
            self.rank[i] = 1

    def union(self, x, y):
        n1, n2 = self.find(x), self.find(y)

        if n1 == n2:
            return False
        if self.rank[n1] > self.rank[n2]:
            self.par[n2] = n1
        elif self.rank[n2] > self.rank[n1]:
            self.par[n1] = n2
        else:
            self.par[n2] = n1
            self.rank[n1] += 1

        return True

    def find(self, x):
        p = self.par[x]

        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]

        return p

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        for i, e in enumerate(edges):
            e.append(i)

        edges.sort(key=lambda e:e[2])

        mst_weight = 0

        uf = UnionFind(n)
        for v1, v2, w, i in edges:
            if uf.union(v1, v2):
                mst_weight += w

        critical, psuedo = [], []

        for n1, n2, ew, i in edges:
            weight = 0
            k = 0
            uf = UnionFind(n)
            for v1, v2, w, j in edges:
                if i != j and uf.union(v1, v2):
                    weight += w
                    k += 1

            if k != n - 1 or weight > mst_weight:
                critical.append(i)
                continue
            
            uf = UnionFind(n)
            weight = ew
            uf.union(n1, n2)
            for v1, v2, w, j in edges:
                if uf.union(v1, v2):
                    weight += w

            if weight == mst_weight:
                psuedo.append(i)

        return [critical, psuedo]