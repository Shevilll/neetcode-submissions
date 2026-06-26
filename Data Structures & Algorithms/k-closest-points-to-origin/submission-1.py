class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        temp = []
        for x, y in points:
            temp.append((x**x + y**y, x, y))
        heapq.heapify(temp)
        res = []
        for i in range(k):
            res.append(list(heapq.heappop(temp)[1:]))
        
        return res