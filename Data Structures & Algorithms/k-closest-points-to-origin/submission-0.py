class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heapq.heapify(points)
        res = []
        for i in range(k):
            res.append(heapq.heappop(points))
        
        return res