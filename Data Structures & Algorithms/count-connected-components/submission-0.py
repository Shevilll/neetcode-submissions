class UnionFind:
    def __init__(self, n):
        self.par = {i:i for i in range(n)}
        self.rank = {i:0 for i in range(n)}
    
    def find(self, x):
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x

    def union(self, x, y):
        p1, p2 = self.find(x), self.find(y)

        if p1 == p2:
            return False
        
        if self.rank[p1] > self.rank[p2]:
            self.par[p1] = p2
        elif self.rank[p2] > self.rank[p1]:
            self.par[p2] = p1
        else:
            self.par[p1] = p2
            self.rank[p1] += 1
        
        return True
    

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)

        for x, y in edges:
            uf.union(x, y)
        
        res = set()

        for i in range(n):
            res.add(uf.find(i))
        
        return len(res)
