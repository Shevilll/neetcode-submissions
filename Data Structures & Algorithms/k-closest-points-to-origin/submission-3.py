class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []

        temp = []

        for i, j in points:
            dist = ((i**2) + (j**2))**0.5
            temp.append((dist, i, j))

        temp.sort()

        for i in range(k):
            if i < len(temp):
                res.append([temp[i][1], temp[i][2]])
        
        return res